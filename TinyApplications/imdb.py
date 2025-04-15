import requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0"}
html=requests.get(url,headers=headers).content
soup=BeautifulSoup(html,"html.parser")
liste=soup.find("ul",{"class":"ipc-metadata-list"}).find("li")
for item in liste:
    # print(item)
    filmadi=item.find("h3",{"class":"ipc-title__text"}).text
    puan=item.find("span",{"class":"ipc-rating-star"}).text
    print(puan)
# print(liste) #403 forbidden hatası








