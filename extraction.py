import urllib
import pandas as pd
from bs4 import BeautifulSoup


# start of main program to create dataframe
title = list()
body = list()

data = pd.read_csv("OnlineNewsPopularity.csv")

for i in range(0,len(data)-1):
    r = urllib.urlopen(data.iloc[i,0])
    soup = BeautifulSoup(r)
    
    try:
        title.append(soup.body.div.article.header.h1.get_text())
    except AttributeError as exp:
        title.append(None)
    
    try:
        body.append(soup.body.div.article.section.get_text())
    except AttributeError as exp:
        body.append(None)

content = pd.DataFrame({'Title': title, 'Body': body})

# save contents to csv file 
content.to_csv('content.csv', sep=',', encoding='utf-8')

