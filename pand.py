import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.flipkart.com/search?q=refrigerator&sid=j9e%2Cabm%2Chzg&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=refrigerator%7CRefrigerators&requestId=d1a389a0-c817-490c-bd92-3681bb993207&as-searchtext=refred"
nm=[]
pr=[]
rt=[]
product=[]
req=requests.get(url)
content=BeautifulSoup(req.content,"html.parser")
product=content.find_all('div',{'class':'_4rR01T'})
price=content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
ratting=content.find_all('div',{'class':'_3LWZlK'})
for i in range(22):
    nm.append(product[i].text)
for i in range(22):
    pr.append(price[i].text)
for i in range(22):
    rt.append(ratting[i].text)
data={'Name':nm,'Price':pr,'Ratting':rt}
df=pd.DataFrame(data)
df.to_csv('product.csv',index=False,encoding='utf-8')