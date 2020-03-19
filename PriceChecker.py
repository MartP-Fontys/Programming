import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/dp/B07GDR2LYK/ref=sxin_2_ac_d_rm?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ac_md=0-0' \
      '-c29ueQ%3D%3D-ac_d_rm&cv_ct_cx=sony&keywords=sony&pd_rd_i=B07GDR2LYK&pd_rd_r=503c5543-1744-4923-949d' \
      '-9b8e958f5da4&pd_rd_w=a7YNq&pd_rd_wg=8OKDU&pf_rd_p=41e4a735-f85d-40a9-a690-f79888fd3edb&pf_rd_r' \
      '=AC2CWGDJWQ7YE2W0BZZY&psc=1&qid=1584008247 '

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    if converted_price < 200:
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo

    server.login('martpeters28@gmail.com', 'vcxshxejgmrwuerw')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.nl/Sony-WH-1000XM3-Cancelling-koptelefoon-snellaadfunctie/dp' \
           '/B07GDR2LYK/ref=br_asw_pdt-3?pf_rd_m=A17D2BRD4YMT0X&pf_rd_s=&pf_rd_r=3D51F1NK7V8F23VPFHE1&pf_rd_t=36701' \
           '&pf_rd_p=721e2053-792d-4e52-8c46-32c76134be82&pf_rd_i=desktop '

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'martpeters28@gmail.com',
        'martpeters28@live.nl',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while(True):
    check_price()
    time.sleep(60 * 60)
