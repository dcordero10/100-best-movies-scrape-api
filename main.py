from bs4 import BeautifulSoup
import requests
import re

###MAKE SOUP
URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
gallery = soup.select_one(selector=".listicle-container")

###GET ALL MOVIES
all_images = gallery.select(selector=".image-container img")
all_movies = []
for image in all_images:
    all_movies.append(image.get("alt"))

###GET ALL YEARS
years_var = gallery.select("p", name="strong")
all_years = []

for item in years_var:
    year_test = re.split('[< >]', str(item))[4]

    if len(year_test) == 4:
        all_years.append(year_test)


links_var = gallery.find_all("a")
all_links = []
for item in links_var:
    link = str(item).split('"')
    cleaned_link = link[1]
    if "https://www.empireonline.com/movies/reviews/" in cleaned_link:
        print(cleaned_link)
        all_links.append((cleaned_link))
    else:
        print(item)


SHEETY_API_ENDPOINT = "https://api.sheety.co/802ab903566d952628c23c0c93790639/topMovies/movies"

print(len(all_links))
print(len(all_movies))
print(len(all_years))

for x in range(0,100):
    new_row = {
        "movie": {
            "title": all_movies[x],
            "year": all_years[x],
            "review": all_links[x],
        }
    }
    response = requests.post(url=SHEETY_API_ENDPOINT, json=new_row)
    response.raise_for_status()
