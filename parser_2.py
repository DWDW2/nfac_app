response = '''<li>
            <a href="https://sxodim.com/almaty" class="city_button"><span class="city-choice-title">Алматы</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/astana" class="city_button"><span class="city-choice-title">Астана</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/shymkent" class="city_button"><span class="city-choice-title">Шымкент</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/bishkek" class="city_button"><span class="city-choice-title">Бишкек</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/turkistan" class="city_button"><span class="city-choice-title">Туркестан</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/karaganda" class="city_button"><span class="city-choice-title">Караганда</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/aktobe" class="city_button"><span class="city-choice-title">Актобе</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/aksu" class="city_button"><span class="city-choice-title">Аксу</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/aktau" class="city_button"><span class="city-choice-title">Актау</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/atyrau" class="city_button"><span class="city-choice-title">Атырау</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/zhanaozen" class="city_button"><span class="city-choice-title">Жанаозен</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/zhezkazgan" class="city_button"><span class="city-choice-title">Жезказган</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/kokshetau" class="city_button"><span class="city-choice-title">Кокшетау</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/kostanay" class="city_button"><span class="city-choice-title">Костанай</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/kyzylorda" class="city_button"><span class="city-choice-title">Кызылорда</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/pavlodar" class="city_button"><span class="city-choice-title">Павлодар</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/petropavlovsk" class="city_button"><span class="city-choice-title">Петропавловск</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/ridder" class="city_button"><span class="city-choice-title">Риддер</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/rudnyi" class="city_button"><span class="city-choice-title">Рудный</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/semey" class="city_button"><span class="city-choice-title">Семей</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/talgar" class="city_button"><span class="city-choice-title">Талгар</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/taldykorgan" class="city_button"><span class="city-choice-title">Талдыкорган</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/taraz" class="city_button"><span class="city-choice-title">Тараз</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/temirtau" class="city_button"><span class="city-choice-title">Темиртау</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/uralsk" class="city_button"><span class="city-choice-title">Уральск</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/ustkamenogorsk" class="city_button"><span class="city-choice-title">Усть-Каменогорск</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/ekibastuz" class="city_button"><span class="city-choice-title">Экибастуз</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/tashkent" class="city_button"><span class="city-choice-title">Ташкент</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/osh" class="city_button"><span class="city-choice-title">Ош</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/stepnogorsk" class="city_button"><span class="city-choice-title">Степногорск</span></a>
        </li> 
        <li>
            <a href="https://sxodim.com/saran" class="city_button"><span class="city-choice-title">Сарань</span></a>
        </li></ul>'''


import json
from bs4 import BeautifulSoup
import requests

def parse_cities(url):
    try:
        # Получаем HTML-код страницы по указанному URL
         # Проверяем успешность запроса

        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response, 'html.parser')

        # Находим все теги <li> с классом "city"
        cities_tags = soup.find_all('li')

        # Извлекаем текст из каждого тега <li> и добавляем его в список
        cities = [city.get_text(strip=True) for city in cities_tags]

        links = soup.find_all('a', href=True)

        # Extract href attributes from the <a> tags and store them in a list
        hrefs = [link['href'] for link in links]
        events_url = {}
        for i in range(len(cities)):
            events_url[cities[i]] = hrefs[i]
        return events_url
        
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def write_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data has been successfully written to {filename}.")
    except IOError as e:
        print(f"Error writing to {filename}: {e}")

# Пример использования парсера и записи в JSON-файл
if __name__ == "__main__":
    url = 'https://example.com/cities'  # Замените на реальный URL страницы с городами
    cities = parse_cities(url)
    if cities:
        write_to_json(cities, 'cities.json')
    else:
        print("Не удалось получить список городов.")
