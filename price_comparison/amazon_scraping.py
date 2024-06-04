import requests
from bs4 import BeautifulSoup

# Function to scrape Amazon
def scrape_amazon(product_name):
    headers = {"Give your user agent"}
    product_name = '+'.join(product_name.split())
    amazon_url = f'https://www.amazon.in/s?k={product_name}'
    response = requests.get(amazon_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    products = []
    for item in results:
        name = item.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
        try:
            price = item.find('span', class_='a-price-whole').text.strip()
        except AttributeError:
            price = "Price not available"
        products.append({'Name': name, 'Price': price})  
    return products





