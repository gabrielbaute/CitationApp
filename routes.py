from flask import render_template, request, jsonify, redirect, url_for
from citation_api import crossref_doi, get_book_by_isbn, get_webpage_metadata
from forms import ReferenceForm
from formatters import format_reference, format_book, format_webpage

def setup_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html', title='Bienvenido')

    @app.route('/generate_reference', methods=['GET', 'POST'])
    def generate_reference():
        form = ReferenceForm()
        if form.validate_on_submit():
            doi_link = form.link.data
            style = form.style.data

            doi = doi_link.split('doi.org/')[1] if 'doi.org/' in doi_link else doi_link
            bib_data = crossref_doi(doi)
            if "error" in bib_data:
                return jsonify({"error": bib_data["error"]}), 400

            reference = format_reference(style, bib_data)
            return redirect(url_for('reference', style=style, reference=reference))

        return render_template('generate_reference.html', form=form)

    @app.route('/generate_book_reference', methods=['POST'])
    def generate_book_reference():
        isbn = request.form['isbn']
        style = request.form['style']

        book_data = get_book_by_isbn(isbn)
        if "error" in book_data:
            return jsonify({"error": book_data["error"]}), 400

        reference = format_book(book_data, style)
        return redirect(url_for('reference', style=style, reference=reference))

    @app.route('/generate_web_reference', methods=['POST'])
    def generate_web_reference():
        url = request.form['url']
        style = request.form['style']

        metadata = get_webpage_metadata(url)
        if "error" in metadata:
            return jsonify({"error": metadata["error"]}), 400

        reference = format_webpage(metadata, style)
        return redirect(url_for('reference', style=style, reference=reference))

    @app.route('/reference')
    def reference():
        style = request.args.get('style')
        reference = request.args.get('reference')
        return render_template('reference.html', style=style, reference=reference)

    @app.route('/all_reference', methods=['POST'])
    def all_reference():
        doi_link = request.form['link']
        doi = doi_link.split('doi.org/')[1] if 'doi.org/' in doi_link else doi_link

        bib_data = crossref_doi(doi)
        if "error" in bib_data:
            return jsonify({"error": bib_data["error"]}), 400
        
        styles = ['APA', 'Vancouver', 'Chicago', 'MLA', 'Harvard', 'IEEE', 'UNE-ISO 690:2024']
        references = {style: format_reference(style, bib_data) for style in styles}

        return render_template('all_reference.html', references=references)

    @app.route('/documentation')
    def documentation():
        return render_template('documentation.html', title='Documentación')
