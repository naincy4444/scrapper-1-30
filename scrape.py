# python -m pip install requests
# => get data from web(html, json, xml)
# python -m pip install beautifulsoup4
# => parse html


# First Time
# Install git
# git config --global user.name "Naincy Ghale"
# git config --global user.email "naincy.2n2k@gmail.com"
# create respiratiry in github
# copypaste git cide from github

# Always
# git add .
# git commit -m "Finish project"

##################
# 1. change the code.
# 2. git add .
# 3. git commit -m "Your message"
# 4. git push
#####################


import json
import requests 
from bs4 import BeautifulSoup 


url = "https://books.toscrape.com/"

all_books = []

def scrape_books(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        return
    
    # Set encoding explicitly to handle special characters c
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        print(title)
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = price_text[1:]
        book = {
            "title": title,
            "currency": currency,
            "price": price,
        }

        all_books.append(book)

    return all_books

all_books = scrape_books(url)

with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(all_books, f, indent = 2, ensure_ascii=False)