import requests

from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com/")

content = response.content

site = BeautifulSoup(content, "html.parser")

noticia = site.find("div", class_="feed-post-body")

#titulo = noticias.find("a", attrs={"class": "feed-post-link"})
#print(titulo.text)

if noticia:
    # Título
    titulo = noticia.find("a", class_="feed-post-link")
    if titulo:
        print("Título:", titulo.text.strip())

    # Subtítulo
    subtitulo = noticia.find("div", class_="feed-post-body-resumo")
    if subtitulo:
        print("Subtítulo:", subtitulo.text.strip())
else:
    print("Nenhuma notícia encontrada.")


 
