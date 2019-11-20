import requests 
from bs4 import BeautifulSoup
import smtplib
import time

URL = input('Insert the Amazon link of desired product: ')

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

def checkPrice():
    page = requests.get(URL, headers=headers)

    content = page.content

    soup = BeautifulSoup(content, 'lxml')
    title = soup.find(id="productTitle")
    price = soup.find(id='priceblock_ourprice')
    rmvE = price.get_text().replace('€','')
    converted_price = float(rmvE[0:].replace(',', ''))
    print(title.get_text().strip())
    print(converted_price)
    originalPrice = input('Insert the original price: ')
    if converted_price < originalPrice :
        sendMail()

def sendMail():
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    
    server.login('email1', 'pass')

    subject = 'Price Fell Down!'
    body = f'The price is {rmvE}€, check amazon Link: {URL}'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email1',
        'email2',
        msg 
    )

    print('Email has been sent!!!')
    server.quit()

while True:
    checkPrice()
    time.sleep(60 * 60)

