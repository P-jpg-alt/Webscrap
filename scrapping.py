import requests
from bs4 import BeautifulSoup
class project:
    def __init__(self,url):
        self.url=l 
        
l=input("Enter URL:")
p=project(l)


# Step 1: Get the HTML
r = requests.get(l)
htmlContent = r.content
print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

# Step 3: HTML Tree traversal 
print(type(title)) 


# Get the title of the HTML page
title = soup.title
print(title)

# Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)

print(anchors)

# Get first element in the HTML page
print(soup.find('p') ) 

# Get classes of any element in the HTML page
#print(soup.find('p')['class'])



# Get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "l" +link.get('href')
        all_links.add(link)
        print(linkText)
