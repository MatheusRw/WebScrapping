import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://g1.globo.com/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

lista_noticias = []

noticias = soup.find_all("div", class_="feed-post-body")

for noticia in noticias:
    titulo_tag = noticia.find("a", class_="feed-post-link")
    subtitulo_tag = noticia.find("div", class_="feed-post-body-resumo")

    titulo = titulo_tag.get_text(strip=True) if titulo_tag else None
    subtitulo = subtitulo_tag.get_text(strip=True) if subtitulo_tag else None

    lista_noticias.append({
        "titulo": titulo,
        "subtitulo": subtitulo
    })

# cria dataframe
news = pd.DataFrame(lista_noticias)

# garante ordem das colunas
news = news[["titulo", "subtitulo"]]

# remove linhas sem titulo
news = news.dropna(subset=["titulo"])

print(news.to_string(index=False))

news.to_excel("noticias.xlsx", index=False)