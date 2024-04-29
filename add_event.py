from app_init import FDataBase
from parser1 import Parser_n


base_url = "https://sxodim.com/astana"

parser = Parser_n(base_url=base_url)
selector_img = 'div.page-content div.impression-card-image img'
link_selector = 'div.page-content div.impression-card-image a'
selector_descr = 'div.content-wrapper p'
title_selector = 'div.page-content div.impression-card-image a.impression-card-title'

soup = parser.create_soup(url="https://sxodim.com/astana")

arr_of_img = parser.extract_image_src(soup=soup, img_selector=selector_img)
arr_of_descr = parser.parse_descr(soup=soup, link_selector=link_selector, desc_selector=selector_descr, desc_limit=2)
arr_of_titles = parser.get_titles(soup=soup, title_selector=title_selector)

print(f"{arr_of_img} \n {arr_of_descr} \n {arr_of_titles} ")