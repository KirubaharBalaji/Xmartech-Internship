from html_scrapper import crawl_html
from sitemap_scrapper import scrape_sitemap
from writer import write_to_file

        
sitemap_url = ["https://atozserver.com/sitemap_index.xml","https://intimatehygine.com/sitemap_index.xml","https://voiceofadventure.com/sitemap_index.xml","https://byteoverflow.com/sitemap_index.xml","https://upashanayoga.com/sitemap_index.xml"]
#sitemap_url="https://atozserver.com/sitemap_index.xml"
for link in sitemap_url:
    #to access the list of sitemap urls
    result = scrape_sitemap(link)
    if result:
        for xml in result:
            result1=scrape_sitemap(xml)
            if result1:     
                print(f"\n\n Scraped URLs from Sitemap XML: \n\n\n{xml}:\n\n")
            for url in result1:
                print(url)
            result = crawl_html(url)

