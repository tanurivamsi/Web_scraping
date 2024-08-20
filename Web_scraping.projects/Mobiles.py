import requests
from bs4 import BeautifulSoup
import pandas
import csv

url="https://www.flipkart.com/tyy/4io/~cs-gcxawvd1ly/pr?sid=tyy%2C4io&collection-tab-name=+vivo+T2+Pro+5G&param=8992&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTIwLDk5OSoiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJ2aXZvIFQyIFBybyA1ZyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdUNFJaTVpGRVdEWTciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19"
web_page=requests.get(url)

soup=BeautifulSoup(web_page.text,"html.parser")
#print(soup.text)


name=soup.find_all("div",class_="KzDlHZ")
names=[]
for i in name:
    j=i.text
    names.append(j)
    #print(names)


price=soup.find_all("div",class_="hl05eU")
prices = []
for i in price:
    j=i.get_text()
    prices.append(j)
    #print(prices)


rating=soup.find_all("div",class_="XQDdHH")
#print(rating)
ratings = []
for i in rating:
    j=i.text
    ratings.append(j)
    #print(ratings)


future=soup.find_all("div",class_="_6NESgJ")
futures = []
for i in future:
    j=i.text
    futures.append(j)
    #print(futures)


review=soup.find_all("span",class_="Wphh3N")
reviews = []
for i in review:
    j=i.text
    reviews.append(j)
    #print(reviews)

data={
    'Product_Names':names,
    'Prices':prices,
    'Ratings':ratings,
    'features':futures,
    'Reviews':reviews

}

df = pandas.DataFrame(data)
print(df)

df.to_csv("Mobiles_Data1.xlsx")
