from bs4 import BeautifulSoup
import csv

url = 'https://www.beautifulshop.com'


soup = BeautifulSoup('html.parser')

links = soup.find_all('a')
link_text = [link.text for link in links]

with open('links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text"])
    for text in link_text:
        writer.writerow([text])



