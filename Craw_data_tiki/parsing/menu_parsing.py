from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen


all_list = []


def menu_extract(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')

    # MENU GENERAL
    menu_general = soup.find("div", attrs={"class":re.compile('bKBPyH')})
    
    # Lặp qua từng phần tử trong menu_general
    for general in menu_general:
        menu_list = general.find_all("div", attrs={"class":re.compile('hagwli')})
        
        for menu in menu_list:
            menu_item = menu.find_all('a', href=True)
            if menu_item:  # Kiểm tra nếu menu_item không rỗng
                all_list.append(menu_item[0]['href'])

    return all_list

def main():
    website_path = 'https://tiki.vn/'
    all_category = menu_extract(website_path)
    print(all_category)
    return all_category

if __name__ == "__main__":
    main()