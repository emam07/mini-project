import requests
from bs4 import BeautifulSoup
url="https://allfamousbirthday.com"
r=requests.get(url)
htmlcontent= r.content
#print(htmlcontent)
soup= BeautifulSoup(htmlcontent,'html.parser')
print(soup.prettify)
title= soup.title
#print(type(title))
anchors=soup.find_all('a')
all_links=set()
paras=soup.find("p")
#print(paras,['class'])
#print(soup.get_text())
for link in anchors:
    if (link.get('href')!="#"):
        linktext="https://allfamousbirthday.com"+link.get('href')
        all_links.add(link)
       # print(linktext)
markup='<p><!--this is a comment for you naruto--></p>'
soup2= BeautifulSoup(markup)
print(soup2.p.string)
exit() 