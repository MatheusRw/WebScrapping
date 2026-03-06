import requests

from bs4 import BeautifulSoup

response = requests.get("https://g1.globo.com/")

content = response.content

site = BeautifulSoup(content, "html.parser")

noticias = site.find_all("div", class_="feed-post-body")

titulo = noticia.find("a", attrs={"class": "feed-post-link"})
print(titulo.text)

subtitulo = noticia.find("div", attrs={"class": "feed-post-body-resumo"})
print(subtitulo.text)