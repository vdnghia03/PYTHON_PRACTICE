from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib
import pandas as pd


# Define product info data
class product_info:
    def __init__(self, cagetory, price, title, discount, rating, total_sales, prod_id):
        self.category =category
        self.price = price
        self.title = title
        self.discount = discount
        self.total_sales = total_sales
        self.rating = rating
        self.prod_id = prod_id

# Define Link product
class product_link:
    def __init__(self, image, product):
        self.image = image
        self.product = product

# got link extract from menu and number of page from main_build.py

def process_page(website_path, link, i):
    tuple_data = []
    tuple_data_page = []

    # Config
    request_url = website_path + link + "?page="+str(i)
    html = urlopen(request_url)
    bs = BeautifulSoup(html, 'html.parser')

    list_prod_id = bs.find_all("div", attrs={"class":re.compile('gjLnmh')})

    



    tuple_data = tuple([

    ]
    )
    tuple_data.append(product_data)
