# 📚 CitationApp

![License](https://img.shields.io/badge/license-MIT-brightgreen)

CitationApp es una herramienta versátil que genera referencias bibliográficas en múltiples estilos (APA, MLA, Chicago, Vancouver, Harvard, IEEE, y UNE-ISO 690:2024) a partir de DOI, ISBN y URLs de páginas web.

## 🚀 Características

- **Generación por DOI:** Obtiene datos bibliográficos a partir de un DOI.
- **Generación por ISBN:** Obtiene datos bibliográficos de libros a partir de un ISBN.
- **Generación por URL:** Extrae metadatos de páginas web para generar referencias.
- **Todos los formatos:** Muestra las referencias en todos los formatos soportados.

## 📑 Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/gabrielbaute/CitationApp
    cd CitationApp
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    pip install -r requirements.txt
    ```

## 📝 Uso

1. Ejecuta la aplicación Flask:
    ```sh
    flask run
    ```

2. Abre tu navegador y ve a `http://localhost:5000` para acceder a la aplicación.

## 📂 Estructura del Proyecto

```
CitationApp/
│
├── app.py
├── routes.py
├── citation_api.py
├── formatters.py
├── forms.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── generate_reference.html
│   ├── reference.html
│   └── all_reference.html
│
└── static/
    └── css/
        └── custom.css
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

Desarrollado con ❤️ en Python por [Gabriel Fernando](https://github.com/gabrielbaute)