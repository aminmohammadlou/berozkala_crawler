from bs4 import BeautifulSoup
import requests
import re

from products.models import Category, Product


def category_crawler():
    base_url = "https://berozkala.com"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, features='html.parser')
    result_set = soup.select("#navigation > ul > li > a")
    categories = []
    for page_element in result_set:
        s = BeautifulSoup(str(page_element), features='html.parser')
        for a in s.find_all('a', href=True):
            categories.append(Category(a.text.strip(), base_url + a['href']))

    del categories[0]
    return categories


def product_crawler(category):
    response = requests.get(category.url)
    soup = BeautifulSoup(response.text, features='html.parser')
    names = soup.select(
        '#mweb-site-wrap > div > div > div > div.content-wrap.content-with-sidebar.col-md-27.col-xs-36 > nav > ul > '
        'li > div > div > div.product-detail-area > h3 > a')
    prices = soup.select(
        '#mweb-site-wrap > div > div > div > div.content-wrap.content-with-sidebar.col-md-27.col-xs-36 > nav > ul > '
        'li > div > div > div.product-detail-area > span > ins > span')

    products = []
    for name, price in list(zip(names, prices)):
        products.append(Product(name=name.text, price=int(re.sub("\\D", "", price.text)), category=category))

    return products
