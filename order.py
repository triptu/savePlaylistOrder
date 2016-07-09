'''Sometimes we download videos from playlist and then we forget their order.
This program solves that problem. Give the playlist link and it will make
a text document with the order of videos.'''

import requests
from bs4 import BeautifulSoup
op=open("playlist link.txt")
link =""
for line in op:
    link =line
    break
playlist= requests.get(link)
soup=BeautifulSoup(playlist.text, "html.parser")
videos= open("order.txt", "w")
count=1
for a in soup.find_all('a', {'class':'pl-video-title-link'}):
    a=str(a)
    name=a[295:].rstrip("</a>").lstrip().rstrip()
    name=str(count)+". "+name
    videos.write( name+ "\n")
    print (name)
    count+=1
videos.close()
