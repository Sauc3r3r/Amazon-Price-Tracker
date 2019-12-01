from urllib.request import urlopen
from bs4 import BeautifulSoup
import smtplib

URL ='https://www.amazon.co.uk/Microsoft-Surface-12-3' \
     '-Tablet-Platinum/dp/B07Y5M67K7/ref=sr_1_4?keywords' \
     '=microsoft+surface&qid=1573669163&s=electronics&sr=8-4'                           #url of amazon product

def check_price():                  #function that reads the url and obtains the price from it
    page = urlopen(URL)
    Python_instructions = BeautifulSoup(page, 'lxml')

    soup = Python_instructions.find(id='priceblock_ourprice' ).get_text()
    price = float(soup.strip()[1:8])
    print(price)

    if price < int(price) - 100:
        send_email()

def send_email():                                   #function that deals with sending the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.ehlo()

    server.login('insert your gmail', 'insert your password' )

    subject = 'Price fell down'         #subject of the email
    body = "check the amazon link I've sent you, 'https://www.amazon.co.uk/" \            #email body
           "Microsoft-Surface-12-3-Tablet-Platinum/dp/B07Y5M67K7/ref=sr_1_4?key" \
           "words=microsoft+surface&qid=1573669163&s=electronics&sr=8-4"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('email receiving the price update',
        "sender's email",
        msg)

    server.quit()

    print('Hey, email has been sent')           #message printed by python showing that the email's been sent

check_price()
