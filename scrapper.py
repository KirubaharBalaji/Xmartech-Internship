
import requests
from lxml import etree


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


sitemap_url = ["https://atozserver.com/sitemap_index.xml","https://intimatehygine.com/sitemap_index.xml","https://voiceofadventure.com/sitemap_index.xml"]
for link in sitemap_url:
    #to access the list of sitemap urls
    result = scrape_sitemap(link)
    if result:
        print("Scraped URLs:")
        for url in result:
            result1=scrape_sitemap(url)
            if result1:     
                print(f"\n\n Scraped URLs from Sitemap URL: \n\n\n{url}:\n\n")
            for url1 in result1:
                print(url1)
              



