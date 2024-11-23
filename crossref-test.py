from crossref.restful import Works

# Crear una instancia del cliente
works = Works()

# Reemplazar con tu DOI
doi = "10.1177/1363461505052659"

# Obtener datos bibliográficos
bib_data = works.doi(doi)

# Mostrar datos en formato BibTeX (si está disponible)
print(bib_data)