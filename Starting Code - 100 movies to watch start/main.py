import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in movies]
movie_titles.reverse()

with open(file="movies.txt", mode="w", encoding='utf-8') as file:
    for item in movie_titles:
        file.write(f"{item}\n")
