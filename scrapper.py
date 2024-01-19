"""Importing Required Modules"""
import requests
from bs4 import BeautifulSoup
import os
import psycopg2
from bs4 import BeautifulSoup
from lxml import etree
def get_connection():
    try:
        return psycopg2.connect(
            database="mydb",
            user="postgres",
            password="0203",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False
def sql():
    web_url = 'https://atozserver.com'
    web_name = 'atozserver'
    web_sitemap = 'https://atozserver.com/sitemap.xml'
    conn = get_connection()
    cursor = conn.cursor()
    if conn:
        print("Connection to the PostgreSQL established successfully.")
        # cursor.execute(
        #    f"insert into mytable(website_name,website_url,website_sitemap) values({web_name},{web_url},{web_sitemap})")
        cursor.execute(
            f"insert into mytable(website_name,website_url,website_sitemap) values('atozserver','https://atozserver.com','https://atozserver.com/sitemap.xml')")
        cursor.execute('SELECT * FROM mytable;')

        rows = cursor.fetchall()
        # Make the changes to the database persistent
        print(rows)
        conn.commit()
        # Close cursor and communication with the database
        cursor.close()
        conn.close()
    else:
        print("Connection to the PostgreSQL encountered and error.")
def scrape_sitemap(url):
    response = requests.get(url)
    # requests.get gets sends a get response from website
    if response.status_code == 200:
        root = etree.fromstring(response.content)
        # Using the fromstring method to get xml content
        urls = root.xpath("//ns:loc/text()", namespaces={"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"})
        # Getting complete xpath from the URL
        # namespace specifies the sitemap link
        return urls
    else:
        print(f"Failed to fetch sitemap. Status code: {response.status_code}")
        return None
def crawl_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    else:
        print(f"Failed to fetch HTML. Status code: {response.status_code}")
        return None
def scrapeXML(sitemap_url):
    xmls = scrape_sitemap(sitemap_url)
    return xmls
def scrapeURL(xml):
    for urls in xml:
        url = scrape_sitemap(urls)
        return url
def scrapeHTML(urls):
    for url in urls:
        html = crawl_html(url)
        return html
def scrapeCONTENT(htmls):
    for html in htmls:
        content = html.get_text("\n", True)
        print(content)
"""Main Driver Code"""
sitemap_urls = "https://intimatehygine.com/sitemap_index.xml"
xmls = scrapeXML(sitemap_urls)
urls = scrapeURL(xmls)
htmls=scrapeHTML(urls)
content=scrapeCONTENT(htmls)
