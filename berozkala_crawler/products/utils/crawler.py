import os
from os.path import basename

from bs4 import BeautifulSoup
from PIL import Image
import requests
import re

from products.models import Category, Product


def category_crawler():
    base_url = "https://berozkala.com"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, features='html.parser')
    result_set = soup.select("#navigation > ul > li > a")
    for page_element in result_set:
        s = BeautifulSoup(str(page_element), features='html.parser')
        for a in s.find_all('a', href=True):
            Category.objects.create(name=a.text.strip(), url=(base_url + a['href']))


def product_crawler(category):
    response = requests.get(category.url)
    soup = BeautifulSoup(response.text, features='html.parser')
    names = soup.select(
        '#mweb-site-wrap > div > div > div > div.content-wrap.content-with-sidebar.col-md-27.col-xs-36 > nav > ul > '
        'li > div > div > div.product-detail-area > h3 > a')
    prices = soup.select(
        '#mweb-site-wrap > div > div > div > div.content-wrap.content-with-sidebar.col-md-27.col-xs-36 > nav > ul > '
        'li > div > div > div.product-detail-area > span > ins > span')

    images = soup.select(
        '#mweb-site-wrap > div > div > div > div.content-wrap.content-with-sidebar.col-md-27.col-xs-36 > nav > ul > '
        'li > div > div > div.product-image-area > a > img')

    image_path = 'media/products'
    try:
        os.mkdir(image_path)
    except FileExistsError:
        pass
    for name, price, image in list(zip(names, prices, images)):
        image_url = 'https://berozkala.com' + image['src']
        image_file = Image.open(requests.get(image_url, stream=True).raw)
        image_file.save('{}/{}'.format(image_path, basename(image['src'])))

        Product.objects.create(name=name.text, price=int(re.sub("\\D", "", price.text)), category=category,
                               image='{}/{}'.format(image_path.split('/')[1], basename(image['src'])))
