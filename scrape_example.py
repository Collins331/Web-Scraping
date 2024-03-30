from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
############# find title ##########
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title, re.IGNORECASE)
print(title)

########### find 'Name:' and 'Favorite Color:'
name_pattern = "Name: [a-zA-Z]+[^<]?"
name_res = re.search(name_pattern, html, re.IGNORECASE) 
name = name_res.group()

color_pattern = "(Favorite.*Color: [a-zA-Z]+[^\n<]?)"
color_res = re.search(color_pattern, html, re.IGNORECASE) 
color = color_res.group()

###### scheme #####
for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)

print(f"{name}\n{color}")
# Copy all html contents into a file
with open("index.html", "w") as file:
    file.write(html)