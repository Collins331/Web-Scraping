import requests as req
from bs4 import BeautifulSoup as bs

res = req.get('https://www.lincsoftwares.tech')
print(res)

soup = bs(res.content, 'html.parser')
print(soup.prettify())