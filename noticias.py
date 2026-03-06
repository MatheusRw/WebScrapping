import requests
from bs4 import BeautifulSoup

# Faz a requisição
response = requests.get("https://g1.globo.com/")
response.raise_for_status()

# Pega o conteúdo da página
content = response.content
site = BeautifulSoup(content, "html.parser")

# Encontra todas as notícias
noticias = site.find_all("div", class_="feed-post-body")

for noticia in noticias:
    # Título
    titulo = noticia.find("a", class_="feed-post-link")
    if titulo:
        print("Título:", titulo.text.strip())

    # Subtítulo
    subtitulo = noticia.find("div", class_="feed-post-body-resumo")
    if subtitulo:
        print("Subtítulo:", subtitulo.text.strip())

    print("-" * 80)  # separador visual
