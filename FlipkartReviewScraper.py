from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd

def appendMod(var,column):
    if var is not None:
        column.append(var.text)
    else:
        column.append("NA")

link = (input("Enter the link of the desired product: "))
page = req.get(link)
page.content
soup = bs(page.content, 'html.parser')
soup.prettify()
consumer=[]
rating=[]
heading=[]
review=[]
count=0

for data in soup.findAll('div',class_='_16PBlm'):
    names=data.find('p', attrs={'class':'_2sc7ZR _2V5EHH'})
    stars=data.find('div', attrs={'class':'_3LWZlK _1BLPMq'})
    head=data.find('p', attrs={'class':'_2-N8zT'})
    rev=data.find('div', attrs={'class':'t-ZTKy'})
    appendMod(names,consumer)
    appendMod(stars,rating)
    appendMod(head,heading)
    appendMod(rev,review)
    count+=1

df=pd.DataFrame({'Consumer Name':consumer, 'Rating (Out of 5)':rating, 'Heading':heading, 'Review':review})
df.head(count)
df.to_csv("Reviews.csv",index=False)
