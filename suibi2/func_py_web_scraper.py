# func_py_web_scraper.py
import requests
from bs4 import BeautifulSoup

def func_py_web_scraper(url):
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to fetch page"
    soup = BeautifulSoup(response.text, 'html.parser')
    return [a.text for a in soup.find_all('a') if a.text]

print(func_py_web_scraper("https://example.com"))
