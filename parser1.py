import sqlite3
import requests
import re
from bs4 import BeautifulSoup


class Parser_n:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_soup(self, url):
        full_url = f'{url}'
        response = requests.get(full_url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def extract_image_src(self, soup, img_selector):
        array_src = []
        imgs = soup.select(f'{img_selector}')
        for img in imgs:
            array_src.append(img['src'])
        return array_src

    def parse_descr(self, soup, link_selector, desc_selector, desc_limit=None):
        array_desc = []
        links = soup.select(link_selector)
        for link in links:
            href = link['href']
            response = requests.get(href, timeout=1)
            html = response.text
            soup_itter = BeautifulSoup(html, 'html.parser')
            descriptions = soup_itter.select(desc_selector)
            if desc_limit:
                array_desc.extend(descriptions[:desc_limit])
            else:
                array_desc.extend(descriptions)
        return array_desc

    def get_titles(self, soup, title_selector):
        list_of_titles = []
        titles = soup.select(title_selector)
        for title in titles:
            list_of_titles.append(title.text.strip())
        return list_of_titles





