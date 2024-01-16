from bs4 import BeautifulSoup
import requests
from lxml import etree
from writer import write_to_file


def scrape_sitemap(url):
    response = requests.get(url)
    #requests.get gets sends a get response from website
    if response.status_code == 200:
        root = etree.fromstring(response.content)
        # Using the fromstring method to get xml content
        urls = root.xpath("//ns:loc/text()", namespaces={"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"})
        #Getting complete xpath from the URL
        #namespace specifies the sitemap link
        return urls
    else:
        print(f"Failed to fetch sitemap. Status code: {response.status_code}")
        return None
