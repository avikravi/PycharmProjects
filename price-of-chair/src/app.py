__author__ = 'Avi'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.quill.com/quill-brand-kelburne-luxura-faux-leather-computer-desk-chair-black-50859/cbs/54147088.html?effort_code=369&sfcp=1&gclsrc=aw.ds&&cm_mmc=SEM_PLA_SHOP_N_19p_54147088_N_N_N&mcode=SEM_PLA_MISC_19p_54147088_N_N&gclid=Cj0KCQiA7qP9BRCLARIsABDaZziyV_1CjeEj2464En-LOOgNpZaT2ggQ8udn01zVQGMy4tXgrWZctWYaAtqyEALw_wcB")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "priceupdate", "id": "SkuPriceUpdate", "content": "89.99"})
string_price = element.text.strip()

price_without_symbol = string_price[:]

price = float(price_without_symbol)

if price < 200:
    print("I can buy it")
    print("The current price is: {}".format(price))
else:
    print("Do not buy")

# <span class="priceupdate" id="SkuPriceUpdate" content="89.99">89.99</span>