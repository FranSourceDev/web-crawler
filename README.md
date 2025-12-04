# 🕷️ Web Crawler en Python

Un rastreador web sencillo pero potente que navega automáticamente por páginas web, extrae contenido relevante y sigue enlaces dentro del mismo dominio.

## 📋 Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación

1. **Clona o descarga el repositorio:**

```bash
git clone https://github.com/tu-usuario/web-crawler.git
cd web-crawler
```

2. **Instala las dependencias:**

```bash
pip install requests beautifulsoup4
```

O si prefieres usar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows
pip install requests beautifulsoup4
```

## 💻 Uso

### Uso Básico

1. Abre el archivo `web_crawler.py` y modifica la URL de inicio:

```python
START_URL = "https://tu-sitio-web.com"
```

2. Ejecuta el script:

```bash
python web_crawler.py
```

### Uso como Módulo

Puedes importar la clase `WebCrawler` en tus propios scripts:

```python
from web_crawler import WebCrawler

# Crear instancia del crawler
crawler = WebCrawler(
    start_url="https://ejemplo.com",
    max_pages=50,    # Máximo de páginas a visitar
    delay=1          # Segundos entre cada request
)

# Ejecutar el crawling
results = crawler.crawl()

# Guardar resultados en un archivo
crawler.save_results(results, filename="mis_resultados.txt")

# Procesar resultados manualmente
for page in results:
    print(f"Título: {page['title']}")
    print(f"URL: {page['url']}")
    print(f"Headings: {page['headings']}")
    print(f"Preview: {page['preview']}")
```

## ⚙️ Parámetros de Configuración

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| `start_url` | str | - | URL inicial desde donde comenzar el crawling |
| `max_pages` | int | 50 | Número máximo de páginas a rastrear |
| `delay` | float | 1 | Tiempo de espera (en segundos) entre requests |

## 📁 Estructura de los Resultados

El crawler extrae la siguiente información de cada página:

```python
{
    'url': 'https://ejemplo.com/pagina',
    'title': 'Título de la Página',
    'preview': 'Primeros 200 caracteres del contenido...',
    'headings': ['Heading 1', 'Heading 2', 'Heading 3']
}
```

## 📄 Archivo de Salida

Los resultados se guardan en `crawler_results.txt` con el siguiente formato:

```
================================================================================
PÁGINA 1
================================================================================

URL: https://ejemplo.com
Título: Página de Ejemplo

Headings: Bienvenido, Servicios, Contacto

Vista previa:
Este es un ejemplo del contenido de la página...
```

## ⚠️ Consideraciones Éticas

- **Respeta el archivo `robots.txt`** de los sitios web
- **No sobrecargues los servidores** - usa un delay adecuado
- **Verifica los términos de servicio** del sitio antes de crawlear
- Este crawler está diseñado para **uso educativo y personal**

## 🔧 Características

- ✅ Crawling limitado al mismo dominio (evita salir del sitio)
- ✅ Detección y eliminación de URLs duplicadas
- ✅ Manejo de errores robusto
- ✅ User-Agent configurable para evitar bloqueos
- ✅ Delay configurable entre requests
- ✅ Extracción de títulos, headings y contenido

## 📝 Ejemplo de Ejecución

```bash
$ python web_crawler.py

Iniciando crawling desde: https://example.com
Máximo de páginas: 20

[1] Crawleando: https://example.com
[2] Crawleando: https://example.com/about
[3] Crawleando: https://example.com/contact
...

Crawling completado. Total de páginas crawleadas: 20
Resultados guardados en: crawler_results.txt

Resumen:
- URLs visitadas: 20
- Primeras 5 páginas crawleadas:
  1. Example Domain...
  2. About Us...
  3. Contact...
```

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Siéntete libre de usarlo y modificarlo.

