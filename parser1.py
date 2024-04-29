import sqlite3
import requests
import re
from bs4 import BeautifulSoup

class Parser_n:
    def create_soup(url):
        base_url = f'{url}'

        response = requests.get(base_url)

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    def extract_image_src(html_content):
        pattern = re.compile(r'<img.*?src=["\'](.*?)["\'].*?>')
        match = pattern.search(str(html_content))
        
        if match:
            return 'https://sxodim.com' + match.group(1)
        else:
            return None


    def parse_descr(soup):
        array_desc = []

        links = soup.select('div.page-content div.impression-card a')
        for i in range(len(list(links))):
            href = links[i]['href']
            response = requests.get(href)
            html = response.text
            soup_itter = BeautifulSoup(html, 'html.parser')
            description = soup_itter.select('div.content_wrapper p')
            array_desc.extend(list(description[0:3]))
        return array_desc
    def get_title(soup):
        list_of_titles = []
        title = soup.select('div.page-content div.impression-card a.impression-card-title')
        for i in range(len(list(title))):
            list_of_titles.append(title[i].text)
        list_final = [event.strip() for event in list_of_titles]
        return list_final 


soup = Parser_n.create_soup("https://sxodim.com/astana")
#print(Parser_n.get_title(soup=soup))
print(type(list(soup.select('div.impression-card-image a'))))
print(soup.select_one("div.page-content div.impression-card a.impression-card-title").text)


