from django.shortcuts import render
from .amazon_scraping import scrape_amazon
from .ebay_scraping import scrape_ebay

def compare_product_prices(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        amazon_products = scrape_amazon(product_name)
        ebay_products = scrape_ebay(product_name)
        context = {
            'amazon_products': amazon_products,
            'ebay_products': ebay_products,
            'searched_product': product_name
        }
        return render(request, 'price_comparison.html', context)
    else:
        return render(request, 'price_comparison.html')