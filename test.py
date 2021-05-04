import requests
from bs4 import BeautifulSoup
import re

URL = "http://web.archive.org/web/20190627165544/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h2")
print("Printing")
print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]


all_movies = str(all_movies).replace(".","</h2>, ")
cleaned_movies = all_movies.split("</h2>, ")


links_var = soup.find_all("a")
all_links = []

for item in links_var:
    link = str(item).split('"')
    cleaned_link = link[1]
    if "http://web.archive.org/web/20190627165544/https://www.empireonline.com/movies/" in cleaned_link:
        print(cleaned_link)
        all_links.append((cleaned_link))
    else:
        pass




all_cleaned_movies = []
for x in range(1,100,2):
    movie = cleaned_movies[x]
    all_cleaned_movies.append(movie)


SHEETY_API_ENDPOINT = "https://api.sheety.co/802ab903566d952628c23c0c93790639/topMovies/movies2"


for x in range(0,150):
    new_row = {
        "movies2": {
            "title": all_cleaned_movies[x],
            "review": all_links[x+3],
        }
    }
    response = requests.post(url=SHEETY_API_ENDPOINT, json=new_row)
    response.raise_for_status()