from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as req
import time
from itertools import *
import unicodecsv as csv
from datetime import datetime
import numpy as np
import pandas as pd
import mysql.connector
from selenium.webdriver.chrome.options import Options

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

titles=list()
urls=list()
position=list()
companies=list()
keyword=list()
times=list()
device=list()
x=0
i=0

today = datetime.today()
d1 = today.strftime("%Y-%m-%d")

filename='output/output.csv'
f=open(filename,'w',encoding='utf-8')    
headers='date,time,device,keyword,company,position,title,url\n'
f.write(headers)


df=pd.read_csv('input.csv', delimiter = ',')
n=len(df)

for row in df.head(n).itertuples():
    z=str(row.input)
    print(z)
    x=0
    dev=0

    while dev < 2:
        dev=dev+1
        
        if dev ==1:
            opts = Options()
            opts.set_capability("browser.cache.disk.enable", False)
            opts.set_capability("browser.cache.memory.enable", False)
            opts.set_capability("browser.cache.offline.enable", False)
            opts.set_capability("network.http.use-cache", False) 
            opts.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
            opts.add_argument("--incognito")
            driver = webdriver.Chrome(chrome_options=opts)
            driver.delete_all_cookies()

        elif dev==2:
            mobile_emulation = {"deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 }, "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
            chrome_options = Options()
            opts.set_capability("browser.cache.disk.enable", False)
            opts.set_capability("browser.cache.memory.enable", False)
            opts.set_capability("browser.cache.offline.enable", False)
            opts.set_capability("network.http.use-cache", False)
            opts.add_argument("--incognito")
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
            driver = webdriver.Chrome(chrome_options = chrome_options)
            driver.delete_all_cookies()
            x=0

        driver.get('https://google.com/search?q='+ z)

        if dev ==1:
            adresults = driver.find_elements_by_class_name("ads-ad")
        elif dev==2:
            adresults = driver.find_elements_by_class_name("ads-fr")

        for adresult in adresults:

            x=x+1
            if dev == 1:
                linkresults= adresult.find_elements_by_class_name("V0MxL")
            elif dev == 2:
                linkresults= adresult.find_elements_by_class_name("C8nzq")

            if dev == 1:
                title= adresult.find_element_by_tag_name('h3')
            elif dev == 2:
                try: 
                    title = adresult.find_element_by_class_name('PpBGzd')
                except:
                    title = adresult.find_element_by_class_name('cfxYMc')
            
            titleval=title.text
            titleval= titleval.replace(',','')

            for link in linkresults:
                url=link.get_attribute('href')
                position.append(x)
                titles.append(titleval)
                urls.append(url)
                search=str(titleval) + str(url)
                search=search.lower()

                if 'betway' in search: company = 'Betway'
                elif 'william' in search: company = 'Williamhill'
                elif 'ladbrokes' in search: company = 'Ladbrokes'
                elif 'paddypower' in search: company = 'Paddypower'
                elif 'paddy power' in search: company = 'Paddypower'
                elif 'betfair' in search: company = 'Betfair'
                elif 'virgin' in search: company = 'Virginbet'
                elif 'sports-king' in search: company = 'Sports-king'
                elif 'coral' in search: company = 'Gala-Coral'
                elif 'playright' in search: company = 'Playright'
                elif 'skybet' in search: company = 'Skybet'
                elif 'sky bet' in search: company = 'Skybet'
                elif 'jackpotjoy' in search: company = 'Jackpot joy'
                elif 'bet365' in search: company = 'Bet365'
                elif 'betfred' in search: company = 'Betdred'
                elif 'top10sportsbettingsites' in search: company = 'Top10SportsBettingSites'
                elif 'betcompare' in search: company = 'Betcompare'
                elif 'mansionbet' in search: company = 'Mansionbet'
                elif 'rubybet' in search: company = 'Rubybet'
                elif '888' in search: company = '888'
                elif 'mrspin' in search: company = 'MrSpin'
                elif 'novibet' in search: company = 'Novibet'
                elif 'ubet' in search: company = 'Ubet'
                elif 'bestbookies' in search: company = 'Best bookies'
                elif 'lottoland' in search: company = 'Lottoland'
                elif 'ice36' in search: company = 'ICE36'
                elif 'thesunvegas' in search: company = 'The sun vegas'
                elif '10bestcasinos' in search: compay = '10 best casinos'
                elif 'hotbettigsites' in search: company = 'Hot beting sites'
                elif 'freebetsbet' in search: company = 'Free bets betting'
                elif 'unibet' in search: company = 'Unibet'
                elif 'stsbet' in search: company = 'Stsbet'
                elif 'sts' in search: company = 'Stsbet'
                elif 'compare.bet' in search: company = 'Compare bet'
                elif 'monopolycasino' in search: company = 'Monopoly Casino'
                elif 'thebonuslounge' in search: company = 'The bonus lounge'
                elif '777' in search: company = '777'
                elif 'lottogo' in search: company = 'Lottogo'
                elif 'hotbetting' in search:  company='Hotbettingsites'
                elif 'casumo' in search: company = 'Casumo'
                elif 'bestukbettingsites' in search: company = 'Best UK betting sites'
                elif 'quinnbet' in search: company = 'Quinnbet'
                elif 'megacasino' in search: company = 'Megacasino'
                elif 'betoffers' in search: company = 'BetOffers'
                elif 'sportnation' in search: company = 'Sports Nation'
                elif 'olbg' in search: company = 'OLBG'
                elif 'superfreeslotgames' in search: company = 'Super Free Slot Games'
                elif '5starbettingsites' in search: company = '5 star betting sites'
                elif 'betvictor' in search: company = 'BetVictor'
                elif 'mrplay' in search: company = 'Mr Play'
                elif 'betbull' in search: company = 'BetBull'
                elif 'rainbow riches casino' in search: company = 'Rainbow Riches Casino'
                elif 'rainbowrichescasino' in search: company = 'Rainbow Riches Casino'
                else: company = 'Other'

                companies.append(company)
                keyword.append(z)
                times.append(current_time)

                if dev == 1:
                    device.append('Desktop')
                    print('Desktop')
                elif dev == 2:
                    device.append('Mobile')
                    print('Mobile')



        driver.quit()


run=len(urls)

while i < run:
    f.write(d1 + ',' + times[i] + ',' + device[i] + ',' + keyword[i] + ',' + companies[i] + ',' + str(position[i]) + ',' + titles[i] + ',' + urls[i] + '\n')
    i=i+1




mydb = mysql.connector.connect(
    host="eu-cdbr-west-02.cleardb.net",
    user="ba22ee85e45681",
    passwd="8cb20161",
    database="heroku_99b6482f61201f9"
)

#host="remotemysql.com",
#user="IhjHetQdWt",
#passwd="ZiYPT8d5mZ",
#database="IhjHetQdWt"

cur = mydb.cursor(buffered=True)

#cur.execute('''CREATE TABLE PPCRESULTS (date DATE NOT NULL, time TIME NOT NULL, device varchar(14) NOT NULL, keyword varchar(30) NOT NULL, company varchar(30) NOT NULL, position int(3) NOT NULL, title varchar(300) NOT NULL, url varchar(300) NOT NULL)''')



i=0

while i<run:

    a1=d1
    a2=times[i]
    a3=device[i]
    a4=keyword[i]
    a5=companies[i]
    a6=position[i]
    a7=titles[i]
    a8=urls[i]

    cur.execute('''INSERT INTO PPCRESULTS (date, time, device, keyword, company, position, title, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',(a1,a2,a3,a4,a5,a6,a7,a8))

    

    #('''INSERT INTO PPCRESULTS (date, time, device, keyword, company, position, title, url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s),(a1,a2,a3,a4,a5,a6,a7,a8)''')
    mydb.commit()
    i=i+1


cur.close()

