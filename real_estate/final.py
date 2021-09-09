import requests
from bs4 import BeautifulSoup
import pandas as pd
from csv import writer

url="https://www.pararius.com/apartments/amsterdam?ac=1"
response=requests.get(url)
#print(response)
soup=BeautifulSoup(response.content,'html.parser')
#print(soup)
lists=soup.find_all("section",{"class":"listing-search-item"})
with open('info.csv','w',encoding='utf-8',newline='') as f:
    thewriter=writer(f)
    header=['Title','Location','Cost','Area']
    thewriter.writerow(header)
    for list in lists:
        title=list.find("a",{"class":"listing-search-item__link--title"}).text.replace("\n",'')
        address=list.find("div",{"class":"listing-search-item__location"}).text.replace("\n",'')
        price=list.find("span",{"class":"listing-search-item__price"}).text.replace("\n",'')
        area=list.find("span",{"class":"illustrated-features__description"}).text.replace("\n",'')

        info=[title,address,price,area]
        thewriter.writerow(info)
