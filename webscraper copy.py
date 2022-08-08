import csv
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from imageio import save

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json


def extract_bestbuy_record(item):
    # description and url
    urlBefore = item.find('a', href=True)["href"]
    url = "https://www.bestbuy.com" + urlBefore

    name = item.find('a', 'wf-offer-link v-line-clamp').text

    try:
        # price after discount
        price_parent = item.find('div', 'priceView-hero-price priceView-customer-price')
        price_second_parent = price_parent.find('span')
        price = price_second_parent.text
    except AttributeError:
        return ''

    try:
        # price before discount
        realprice_parent = item.find('div', 'pricing-price__regular-price').text
        realprice = realprice_parent[4:]
    except AttributeError:
        return ''

    try:
        # deal percentage
        dealamount_parent = item.find('div', 'pricing-price__savings')
        dealamount = dealamount_parent.text
    except AttributeError:
        return ''
    
    try:
        #image
        image_parent = item.find('div', 'wf-offer-image')
        image_parent_second = image_parent.find('a')['href']
        image = "https://www.bestbuy.com" + image_parent_second
    except AttributeError:
        return ''

    result = (name, url, price, realprice, dealamount, image)

    return result



def main():

    #BestBuy More Deals
    driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    bestbuy_more_deals_records_list = []

    url = "https://www.bestbuy.com/site/misc/deal-of-the-day/pcmcat248000050016.c?id=pcmcat248000050016&acampID=1&ref=212&loc=1&gclid=EAIaIQobChMIlJrBiuW1-QIVlcLCBB2joAAYEAAYASAAEgLCF_D_BwE&gclsrc=aw.ds"
    driver2.get(url)

    soup = BeautifulSoup(driver2.page_source, 'html.parser')
    results = soup.findAll('div', {'class' : 'wf-offer wf-last-offer col-xs-3'})

    for item in results:
        record = extract_bestbuy_record(item)
        if record:
            bestbuy_more_deals_records_list.append(record)

    driver2.close

    # save data to json file

    with open('bestbuy.json', 'w') as w:
        json.dump(bestbuy_more_deals_records_list, w)

main()
