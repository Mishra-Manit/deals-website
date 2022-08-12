from urllib.parse import urlparse
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json


def extract_walmart_record(item):
    # description and url
    urlBefore = item.find('a', href=True)["href"]
    url = "https://www.walmart.com" + urlBefore


    if item.find('span', {'data-automation-id' : 'product-title'}) == None:
        name = ' '
    else:
        name = item.find('span', {'data-automation-id' : 'product-title'}).text

    try:
        # price after discount
        price_parent = item.find('div', {'data-automation-id' : 'product-price'})
        price_second_parent = price_parent.find('div', 'b black f5 mr1 mr2-xl lh-copy f4-l')
        price_third_parent = price_second_parent.text
        price = price_third_parent
    except AttributeError:
        return ''

    try:
        # price before discount
        realprice_parent = item.find('div', {'data-automation-id' : 'product-price'})
        realprice_second_parent = realprice_parent.find('div', 'f7 f6-l gray mr1 ttc strike')
        realprice = realprice_second_parent.text
        
    except AttributeError:
        return ''
    
    try:
        #image
        image_parent = item.find('div', {'data-testid' : 'list-view'})
        image_parent_second = image_parent.find('img')
        image = image_parent_second['src']
    except AttributeError:
        return ''

    result = (name, url, price, realprice, image)

    return result



def main():

    #Walmart Deals
    driver3 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    walmart_records_list = []

    url = "https://www.walmart.com/shop/deals"
    driver3.get(url)

    soup3 = BeautifulSoup(driver3.page_source, 'html.parser')
    results = soup3.findAll('div', {'class' : 'h-100 pb1-xl pr4-xl pv1 ph1'})
    print(results)

    for item in results:
        record = extract_walmart_record(item)
        if record:
            walmart_records_list.append(record)

    driver3.close

    # save data to json file

    with open('walmart.json', 'w') as w:
        json.dump(walmart_records_list, w)

main()
