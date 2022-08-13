from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import json

amazonAffiliateTag = 'manitmishra-20'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/path/to/your_chrome_driver_dir/chromedriver',chrome_options=chrome_options)


def extract_record(item):
    # description and url
    parentUrl = item.find('a', href=True)["href"]
    url = parentUrl + "&tag=" + amazonAffiliateTag

    name = item.find('div', 'DealContent-module__truncate_sWbxETx42ZPStTc9jwySW').text

    try:
        # price after discount
        price_parent = item.find('span', 'a-size-mini')
        price_second_parent = price_parent.find('span', 'a-price')
        price = price_second_parent.find('span', 'a-price-whole').text
    except AttributeError:
        return ''

    try:
        # price before discount
        realprice_parent = item.find('span', 'a-size-small a-color-secondary')
        realprice = realprice_parent.find('span', 'a-price-whole').text
    except AttributeError:
        return ''

    try:
        # deal percentage
        dealamount_parent = item.find('div', 'BadgeAutomated-module__badgeOneLineContainer_yYupgq1lKxb5h3bfDqA-B')
        dealamount = dealamount_parent.find('div',
                                            'BadgeAutomatedLabel-module__badgeAutomatedLabel_2Teem9LTaUlj6gBh5R45wd').text
    except AttributeError:
        return ''
    
    try:
        #image
        image_parent = item.find('div', 'a-row a-spacing-small')
        image_parent_second = image_parent.find('img')
        image = image_parent_second['src']
    except AttributeError:
        return ''

    result = (name, url, price, realprice, dealamount, image)

    return result

def extract_bestbuy_record(item):
    # description and url
    urlBefore = item.find('a', href=True)["href"]
    url = "https://www.bestbuy.com" + urlBefore

    
    if item.find('a', 'wf-offer-link v-line-clamp') == None:
        name = ' '
    else:
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
        image_parent_second = image_parent.find('img')['src']
        image = image_parent_second
    except AttributeError:
        return ''

    result = (name, url, price, realprice, dealamount, image)

    return result



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

    #Amazon
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    records_list = []
    url = "https://amzn.to/3zCO1z9"
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.findAll('div', {'data-testid': 'deal-card'})

    for item in results:
        record = extract_record(item)
        if record:
            records_list.append(record)

    driver.close





    #Bestbuy
    driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    bestbuy_records_list = []

    bestbuy_url = "https://www.bestbuy.com/site/misc/deal-of-the-day/pcmcat248000050016.c?id=pcmcat248000050016&acampID=1&ref=212&loc=1&gclid=EAIaIQobChMIlJrBiuW1-QIVlcLCBB2joAAYEAAYASAAEgLCF_D_BwE&gclsrc=aw.ds"
    driver1.get(bestbuy_url)

    soup1 = BeautifulSoup(driver1.page_source, 'html.parser')

    #deal price
    priceParent = soup1.find('div', "priceView-hero-price priceView-customer-price")
    dealPrice = priceParent.find('span').text

    #original price
    originalPriceParent = soup1.find('div', 'pricing-price__regular-price').text
    originalPrice = originalPriceParent[4:]

    #save amount
    saveAmount = soup1.find('div', 'pricing-price__savings').text

    #url
    urlParent = soup1.find('a', 'wf-offer-link v-line-clamp')['href']
    url = "https://www.bestbuy.com" + urlParent
    
    #image
    img = soup1.find('img', 'wf-image img-responsive sr-only')['src']

    #name
    name = soup1.find('a', 'wf-offer-link v-line-clamp').text

    bestbuy_records_list = (name, url, dealPrice, originalPrice, saveAmount, img)

    driver1.close



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


    #Walmart Deals
    driver3 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    walmart_records_list = []

    url = "https://www.walmart.com/shop/deals"
    driver3.get(url)

    soup3 = BeautifulSoup(driver3.page_source, 'html.parser')
    results = soup3.findAll('div', {'class' : 'h-100 pb1-xl pr4-xl pv1 ph1'})

    for item in results:
        record = extract_walmart_record(item)
        if record:
            walmart_records_list.append(record)

    driver3.close
    


    # save data to json file
    
    with open('test1.json', 'w') as f:
        json.dump(records_list, f)

    with open('bestbuyDealOfDay.json', 'w') as w:
        json.dump(bestbuy_records_list, w)

    with open('bestbuy.json', 'w') as w:
        json.dump(bestbuy_more_deals_records_list, w)

    with open('walmart.json', 'w') as w:
        json.dump(walmart_records_list, w)
    

main()
