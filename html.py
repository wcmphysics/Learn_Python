# HTML
# install bs4 using pip:
# pip install beautifulsoup4
# documentation for bs4:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests
URL = "https://www.cs.cmu.edu/~rgs/alice-I.html" 
html = requests.get(URL, {}).text
soup = BeautifulSoup(html)
alice_book = soup.text
print(alice_book[0:10:1])