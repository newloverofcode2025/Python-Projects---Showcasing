# src/web_scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Web Scraping Results:")
        print(soup.title.string)
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_website('https://www.example.com')