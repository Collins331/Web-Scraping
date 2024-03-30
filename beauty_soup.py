from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"

page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

# links = soup.a
# print(links)
for link in soup.find_all('a'):
    url = "http://olympus.realpython.org"
    print(f'{url}{link.get("href")}')