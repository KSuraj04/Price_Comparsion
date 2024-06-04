import requests
from bs4 import BeautifulSoup

def scrape_ebay(product_name):
    headers = {"Give your user agent}
    url = f'https://www.ebay.com/sch/i.html?_nkw={product_name}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 's-item__info clearfix'})

    products = []
    for item in results:
        name = item.find('div',{'class': 's-item__title'}).text
        price = item.find('span', {'class': 's-item__price'}).text.replace('$','').replace(',','').strip()
        products.append({'Name': name, 'Price': price})

    return products
