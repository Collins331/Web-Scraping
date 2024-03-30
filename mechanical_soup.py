import mechanicalsoup

browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
login_page =  browser.get(url)
login_html = login_page.soup


######
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"


######
profile_page = browser.submit(form, login_page.url)

print(profile_page.soup.title)
# print(f"{profile_page.url} \n{profile_page.soup}")