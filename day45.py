import requests
from bs4 import BeautifulSoup
#url = 'https://codewithharry.com'
#contents = requests.get(url)
#htmlContent = contents.content
#soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify())
#title = soup.title
#print(type(title.string))
#print(type(title))
#print(type(soup))
#print(soup.find('p'))
#print(soup.find('p')['class'])

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
contents = requests.get(url)
htmlContent = contents.content
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify())
movies = soup.find_all(name = "h3", class_ = "title")
print(movies)