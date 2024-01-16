import requests
from bs4 import BeautifulSoup
import os 
from writer import write_to_file

def crawl_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
    else:
        print(f"Failed to fetch HTML. Status code: {response.status_code}")
        return None


target_url = "https://byteoverflow.com/tag/northvolt/"
result = crawl_html(target_url)
html=result.prettify()
text=result.get_text("\n",True)
#print(html)
#tit=result.find(property="og:title")
#print(tit)
pg_title=result.title.string
write_to_file("text.txt",text)
write_to_file("texthtml.txt",html)

#print(type(text))
#print(text)
# Directory 
#directory = f"{pg_title}"
  
# Parent Directory path 
#parent_dir = "D:/Xmartech Internship/"
  
# Path 
#path = os.path.join(parent_dir, directory)  
#os.mkdir(path) 
#print("Directory '% s' created" % directory) 
#with open(os.path.join(path, f"{pg_title}.txt"),"w+x",encoding="utf-8") as file:
#    file.write(text)
