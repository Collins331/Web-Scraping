import mechanicalsoup
from time import sleep

browser = mechanicalsoup.Browser()


for _ in range(10):
    page = browser.get("http://olympus.realpython.org/dice")
    html = page.soup

    tag = html.select("#result")[0]
    print(tag.text)
    sleep(2)