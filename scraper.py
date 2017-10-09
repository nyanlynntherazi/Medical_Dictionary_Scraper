import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from time import sleep
from random import randint
import sqlite3 as sql

links = pd.read_csv('alllink_med_dict.csv', header=None)

for url in links[0]:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    header = soup.find('h2',text=True).text
    content = soup.find('div',attrs={'class':'dd'}).text
    records=[]
    records.append((header, content))

    df = pd.DataFrame(records, columns=['vocab', 'meaning'])
    df = df.astype(str)
    
    sql_con = sql.connect("data.sqlite")

    df.to_sql(name='data',con=sql_con ,if_exists='append')
    for _ in range(0,2): #to control the crawl rate
        sleep(randint(0,2))




