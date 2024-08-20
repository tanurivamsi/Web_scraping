import requests
from bs4 import BeautifulSoup
import pandas
import csv
url="https://www.flipkart.com/sports-fitness/pr?count=40&p%5B%5D=facets.brand%255B%255D%3DThunderFit&p%5B%5D=facets.brand%255B%255D%3DKRX&p%5B%5D=facets.brand%255B%255D%3DAerolite&p%5B%5D=facets.brand%255B%255D%3DHeadly&p%5B%5D=facets.brand%255B%255D%3DLi-Ning&p%5B%5D=facets.brand%255B%255D%3DAdidas&p%5B%5D=facets.brand%255B%255D%3DHero&p%5B%5D=facets.brand%255B%255D%3DYonex&p%5B%5D=facets.brand%255B%255D%3DSG&p%5B%5D=facets.brand%255B%255D%3DSS&p%5B%5D=facets.brand%255B%255D%3DMrf&p%5B%5D=facets.brand%255B%255D%3DNew%2BBalance&sid=dep&otracker=clp_metro_tile3_2_2.metroTile.METRO_TILE3_sport-store_CV2WPR8XLU_wp1"
soup=requests.get(url)
print(soup)

web_page=BeautifulSoup(soup.text,"html.parser")
#print(web_page.text)


title=web_page.find_all('div',class_="")
titles=[]
for i in title:
    j = i.text
    titles.append(j)
    #print(titles)