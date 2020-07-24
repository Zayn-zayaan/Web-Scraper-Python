from bs4 import BeautifulSoup
import requests
import images
from PIL import Image
from io import BytesIO
import os


choice = input("wanna search for web or images?")

if choice == 'web':
    search = input("Enter search term:")
    params = {'q': search}
    r = requests.get("https://www.bing.com/search", params=params)

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find('ol', {'id': 'b_results'})
    links = results.findAll("li", {'class': "b_algo"})

    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]

        if item_text and item_href:
            print(item_text)
            print(item_href)

            children = item.find("h2")
            print("Next sibling of the h2:", children.next_sibling)

elif choice == 'images':
    images.startsearch()

else:
    print("Invalid input")



