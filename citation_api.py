import requests
from bs4 import BeautifulSoup
from crossref.restful import Works, Etiquette

etiquette = Etiquette(
    application_name = 'CittationApp',
    application_version = '0.1.0',
    application_url = 'None',
    contact_email = 'gabrielbaute@gmail.com'
)

works = Works(etiquette=etiquette)

# From DOI
def crossref_doi(doi):
    try:
        data = works.doi(doi)
        return data
    except Exception as e:
        return {"error": str(e)}

def crossref_agency(doi):
    try:
        data = works.agency(doi)
        return data
    except Exception as e:
        return {"error": str(e)}

def crossref_query(bibliographic=None, author=None, publisher_name=None):
    try:
        query = works.query()
        if bibliographic:
            query = query.filter(bibliographic=bibliographic)
        if author:
            query = query.filter(author=author)
        if publisher_name:
            query = query.filter(publisher_name=publisher_name)
        
        data = [item['title'][0] for item in query]
        return data
    except Exception as e:
        return {"error": str(e)}

# From ISBN
def get_book_by_isbn(isbn):
    try:
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        book_data = data.get(f"ISBN:{isbn}", {})
        return book_data
    except Exception as e:
        return {"error": str(e)}

# From webpages
def get_webpage_metadata(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Extraer el título
        title = soup.find("title").get_text() if soup.find("title") else "Sin título"

        # Intentar extraer el autor desde diferentes metadatos y estructuras HTML
        author = "Desconocido"
        author_meta = soup.find("meta", attrs={"name": "author"})
        if author_meta:
            author = author_meta["content"]
        else:
            author_meta = soup.find("meta", property="article:author")
            if author_meta:
                author = author_meta["content"]
            else:
                # Verificar si el div con clase "meta" existe antes de buscar el span
                meta_div = soup.find("div", class_="meta")
                if meta_div:
                    author_span = meta_div.find("span", class_="author")
                    if author_span:
                        author = author_span.get_text()

        # Intentar extraer la fecha de publicación desde diferentes metadatos y estructuras HTML
        publication_date = "Fecha desconocida"
        pubdate_meta = soup.find("meta", attrs={"name": "pubdate"})
        if pubdate_meta:
            publication_date = pubdate_meta["content"]
        else:
            pubdate_meta = soup.find("meta", property="article:published_time")
            if pubdate_meta:
                publication_date = pubdate_meta["content"]
            else:
                # Verificar si el div con clase "meta" existe antes de buscar el span
                meta_div = soup.find("div", class_="meta")
                if meta_div:
                    date_span = meta_div.find("span", class_="date")
                    if date_span:
                        publication_date = date_span.get_text()

        return {"title": title, "author": author, "publication_date": publication_date, "url": url}
    except Exception as e:
        return {"error": str(e)}