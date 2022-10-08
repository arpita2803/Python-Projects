from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding='utf-8') as file:
#    contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify()) #shows properly indented code
# print(soup.a) #shows first anchor tag
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
# print(tag.getText())
# print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select(selector="p a") #select using css selector
# print(company_url)

# name = soup.select(selector="#name") # select using specific id. Need to put # before id value
# print(name)

# headings = soup.select(selector=".heading") # select using specific class. Need to put . before class value
# print(headings)

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
texts = [article_tag.getText() for article_tag in articles]
links = [article_tag.get("href") for article_tag in articles]

scores = soup.find_all(name="span", class_="score")
upvotes = [int(article_score.getText().split()[0]) for article_score in scores]

highest_index = upvotes.index(max(upvotes))
print(texts[highest_index])
print(links[highest_index])

# website url/robots.txt to see what scrapping is allowed. better to use API first if available.
