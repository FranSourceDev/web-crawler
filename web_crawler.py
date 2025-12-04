import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
from collections import deque

class WebCrawler:
    def __init__(self, start_url, max_pages=50, delay=1):
        """
        Inicializa el web crawler
        
        Args:
            start_url: URL inicial para comenzar el crawling
            max_pages: Número máximo de páginas a crawlear
            delay: Tiempo de espera entre requests (en segundos)
        """
        self.start_url = start_url
        self.max_pages = max_pages
        self.delay = delay
        self.visited = set()
        self.to_visit = deque([start_url])
        self.domain = urlparse(start_url).netloc
        
    def is_valid_url(self, url):
        """Verifica si la URL es válida y pertenece al mismo dominio"""
        parsed = urlparse(url)
        return (parsed.netloc == self.domain and 
                parsed.scheme in ['http', 'https'])
    
    def get_links(self, url, html):
        """Extrae todos los links de una página"""
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(url, link['href'])
            if self.is_valid_url(absolute_url):
                links.append(absolute_url)
        
        return links
    
    def extract_content(self, url, html):
        """Extrae contenido relevante de la página"""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extraer título
        title = soup.find('title')
        title = title.get_text().strip() if title else 'Sin título'
        
        # Extraer texto de párrafos
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text().strip() for p in paragraphs[:3]])
        
        # Extraer headings
        headings = [h.get_text().strip() for h in soup.find_all(['h1', 'h2', 'h3'])[:5]]
        
        return {
            'url': url,
            'title': title,
            'preview': text[:200] + '...' if len(text) > 200 else text,
            'headings': headings
        }
    
    def crawl(self):
        """Ejecuta el proceso de crawling"""
        results = []
        
        print(f"Iniciando crawling desde: {self.start_url}")
        print(f"Máximo de páginas: {self.max_pages}\n")
        
        while self.to_visit and len(self.visited) < self.max_pages:
            url = self.to_visit.popleft()
            
            if url in self.visited:
                continue
            
            try:
                print(f"[{len(self.visited) + 1}] Crawleando: {url}")
                
                # Hacer request
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                # Marcar como visitada
                self.visited.add(url)
                
                # Extraer contenido
                content = self.extract_content(url, response.text)
                results.append(content)
                
                # Extraer y añadir nuevos links
                links = self.get_links(url, response.text)
                for link in links:
                    if link not in self.visited:
                        self.to_visit.append(link)
                
                # Respetar delay
                time.sleep(self.delay)
                
            except Exception as e:
                print(f"Error al crawlear {url}: {str(e)}")
                continue
        
        print(f"\nCrawling completado. Total de páginas crawleadas: {len(results)}")
        return results
    
    def save_results(self, results, filename='crawler_results.txt'):
        """Guarda los resultados en un archivo"""
        with open(filename, 'w', encoding='utf-8') as f:
            for i, page in enumerate(results, 1):
                f.write(f"\n{'='*80}\n")
                f.write(f"PÁGINA {i}\n")
                f.write(f"{'='*80}\n\n")
                f.write(f"URL: {page['url']}\n")
                f.write(f"Título: {page['title']}\n\n")
                f.write(f"Headings: {', '.join(page['headings'])}\n\n")
                f.write(f"Vista previa:\n{page['preview']}\n")
        
        print(f"Resultados guardados en: {filename}")


# Ejemplo de uso
if __name__ == "__main__":
    # Configura la URL de inicio
    START_URL = "https://example.com"  # Cambia esto por tu URL
    
    # Crear instancia del crawler
    crawler = WebCrawler(
        start_url=START_URL,
        max_pages=20,  # Número de páginas a crawlear
        delay=1  # Espera 1 segundo entre requests
    )
    
    # Ejecutar crawling
    results = crawler.crawl()
    
    # Guardar resultados
    crawler.save_results(results)
    
    # Mostrar resumen
    print(f"\nResumen:")
    print(f"- URLs visitadas: {len(results)}")
    print(f"- Primeras 5 páginas crawleadas:")
    for i, page in enumerate(results[:5], 1):
        print(f"  {i}. {page['title'][:50]}...")