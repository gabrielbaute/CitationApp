def paper_format_apa(reference):
    try:
        authors = reference.get('author', [])
        if authors:
            author_str = ', '.join([f"{author['family']}, {author['given'][0]}." for author in authors])
        else:
            author_str = "Sin autor"

        issued = reference.get('issued', {})
        year = issued.get('date-parts', [[None]])[0][0]

        title = reference.get('title', ["Sin título"])[0]
        container_title = reference.get('container-title', [""])[0]
        volume = reference.get('volume', "")
        issue = reference.get('issue', "")
        pages = reference.get('page', "")
        doi = reference.get('DOI', "")

        apa_citation = f"{author_str} ({year}). {title}. *{container_title}*, {volume}({issue}), {pages}. https://doi.org/{doi}"
        return apa_citation
    except Exception as e:
        return f"Error al formatear en APA: {str(e)}"

def paper_format_vancouver(reference):
    try:
        authors = reference.get('author', [])
        if authors:
            author_str = ', '.join([f"{author['family']} {author['given'][0]}." for author in authors])
        else:
            author_str = "Sin autor"

        title = reference.get('title', ["Sin título"])[0]
        container_title = reference.get('container-title', [""])[0]
        year = reference.get('issued', {}).get('date-parts', [[None]])[0][0]
        volume = reference.get('volume', "")
        issue = reference.get('issue', "")
        pages = reference.get('page', "")
        doi = reference.get('DOI', "")

        vancouver_citation = f"{author_str}. {title}. {container_title}. {year};{volume}({issue}):{pages}. doi:{doi}"
        return vancouver_citation
    except Exception as e:
        return f"Error al formatear en Vancouver: {str(e)}"

def paper_format_chicago(reference):
    try:
        authors = reference.get('author', [])
        if authors:
            author_str = ' and '.join([f"{author['given']} {author['family']}" for author in authors])
        else:
            author_str = "Sin autor"

        title = reference.get('title', ["Sin título"])[0]
        container_title = reference.get('container-title', [""])[0]
        year = reference.get('issued', {}).get('date-parts', [[None]])[0][0]
        volume = reference.get('volume', "")
        issue = reference.get('issue', "")
        pages = reference.get('page', "")
        doi = reference.get('DOI', "")

        chicago_citation = f"{author_str}. {year}. \"{title}.\" *{container_title}* {volume}, no. {issue} ({pages}). https://doi.org/{doi}."
        return chicago_citation
    except Exception as e:
        return f"Error al formatear en Chicago: {str(e)}"


def paper_format_mla(reference):
    try:
        authors = reference.get('author', [])
        if authors:
            author_str = ', '.join([f"{author['family']}, {author['given']}" for author in authors])
        else:
            author_str = "Sin autor"

        title = reference.get('title', ["Sin título"])[0]
        container_title = reference.get('container-title', [""])[0]
        volume = reference.get('volume', "")
        issue = reference.get('issue', "")
        year = reference.get('issued', {}).get('date-parts', [[None]])[0][0]
        pages = reference.get('page', "")
        doi = reference.get('DOI', "")

        mla_citation = f"{author_str}. \"{title}.\" *{container_title}*, vol. {volume}, no. {issue}, {year}, pp. {pages}. doi:{doi}"
        return mla_citation
    except Exception as e:
        return f"Error al formatear en MLA: {str(e)}"


def paper_format_harvard(reference):
    try:
        authors = reference.get('author', [])
        if authors:
            author_str = ', '.join([f"{author['family']}, {author['given'][0]}" for author in authors])
        else:
            author_str = "Sin autor"

        title = reference.get('title', ["Sin título"])[0]
        container_title = reference.get('container-title', [""])[0]
        volume = reference.get('volume', "")
        issue = reference.get('issue', "")
        year = reference.get('issued', {}).get('date-parts', [[None]])[0][0]
        pages = reference.get('page', "")     
        doi = reference.get('DOI', "")

        harvard_citation = f"{author_str}. ({year}) '{title}', {container_title}, {volume}({issue}), {pages}. doi:{doi}"
        return harvard_citation
    except Exception as e:
        return f"Error al formatear en Harvard: {str(e)}"


def paper_format_ieee(reference):
    try:
        authors = reference.get('author', [])
        if authors:
            author_str = ', '.join([f"{author['given']} {author['family']}" for author in authors])
        else:
            author_str = "Sin autor"

        title = reference.get('title', ["Sin título"])[0]
        container_title = reference.get('container-title', [""])[0]
        volume = reference.get('volume', "")
        issue = reference.get('issue', "")
        year = reference.get('issued', {}).get('date-parts', [[None]])[0][0]
        pages = reference.get('page', "")
        doi = reference.get('DOI', "")

        ieee_citation = f"{author_str}, \"{title},\" {container_title}, vol. {volume}, no. {issue}, pp. {pages}, {year}. doi:{doi}"
        return ieee_citation
    except Exception as e:
        return f"Error al formatear en IEEE: {str(e)}"


def paper_format_iso690(reference):
    try:
        authors = reference.get('author', [])
        if authors:
            author_str = '; '.join([f"{author['family']}, {author['given']}" for author in authors])
        else:
            author_str = "Sin autor"

        title = reference.get('title', ["Sin título"])[0]
        container_title = reference.get('container-title', [""])[0]
        year = reference.get('issued', {}).get('date-parts', [[None]])[0][0]
        volume = reference.get('volume', "")
        issue = reference.get('issue', "")
        pages = reference.get('page', "")
        doi = reference.get('DOI', "")

        iso690_citation = f"{author_str} ({year}). {title}. {container_title}, {volume}({issue}), {pages}. doi:{doi}"
        return iso690_citation
    except Exception as e:
        return f"Error al formatear en UNE-ISO 690:2024: {str(e)}"

def format_reference(style, reference):
    if style == 'APA':
        return paper_format_apa(reference)
    elif style == 'Vancouver':
        return paper_format_vancouver(reference)
    elif style == 'Chicago':
        return paper_format_chicago(reference)
    elif style == 'MLA':
        return paper_format_mla(reference)
    elif style == 'Harvard':
        return paper_format_harvard(reference)
    elif style == 'IEEE':
        return paper_format_ieee(reference)
    elif style == 'UNE-ISO 690:2024':
        return paper_format_iso690(reference)
    else:
        return f"Formato {style} aún no soportado."
    
def format_book(book_data, style):
    try:
        title = book_data.get("title", "Sin título")
        authors = book_data.get("authors", [])
        if authors:
            author_str = ', '.join([author['name'] for author in authors])
        else:
            author_str = "Sin autor"

        publishers = book_data.get("publishers", [])
        if publishers:
            publisher_str = ', '.join([publisher['name'] for publisher in publishers])
        else:
            publisher_str = "Sin editorial"

        year = book_data.get("publish_date", "Sin año")

        if style == "APA":
            citation = f"{author_str} ({year}). {title}. {publisher_str}."
        elif style == "MLA":
            citation = f"{author_str}. {title}. {publisher_str}, {year}."
        # Agregar otros estilos según sea necesario
        else:
            citation = f"Formato {style} aún no soportado para libros."

        return citation
    except Exception as e:
        return f"Error al formatear el libro: {str(e)}"

def format_webpage(metadata, style):
    try:
        title = metadata.get("title", "Sin título")
        author = metadata.get("author", "Desconocido")
        publication_date = metadata.get("publication_date", "Fecha desconocida")
        url = metadata.get("url", "")

        if style == "APA":
            citation = f"{author}. ({publication_date}). {title}. Recuperado de {url}"
        elif style == "MLA":
            citation = f"{author}. \"{title}.\" {publication_date}, {url}."
        # Agregar otros estilos según sea necesario
        else:
            citation = f"Formato {style} aún no soportado para páginas web."

        return citation
    except Exception as e:
        return f"Error al formatear la página web: {str(e)}"
