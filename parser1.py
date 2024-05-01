import json
import requests
from bs4 import BeautifulSoup

def parse_events_from_link(link):
    try:
        response = requests.get(link)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')


        events = {}  
        for event_tag in soup.find_all('div', class_='impression-card'):
            title = event_tag.find('a', class_='impression-card-title').get_text(strip=True)
            description = event_tag.find('div', class_='impression-card-info').get_text(strip=True)
            image_url = event_tag.find('img')
            image_url = 'https://sxodim.com'+image_url['src']
            category = event_tag.find('a', class_='badge').get_text(strip=True)
            url_to_event = event_tag.find('a', class_='impression-card-title')

            events[title] = {'title': title, 'description': description, 'image_url':image_url, 'category':category, 'url_to_event':url_to_event['href']}

        return events
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def parse_events_from_json(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        events_by_city = {}
        for city, link in data.items():
            events = parse_events_from_link(link)
            if events:
                events_by_city[city] = events

        return events_by_city
    except IOError as e:
        print(f"Error reading JSON file: {e}")
        return None


if __name__ == "__main__":
    json_file = 'cities.json'  
    events_by_city = parse_events_from_json(json_file)
    if events_by_city:
        with open('events.json', 'w', encoding='utf-8') as f:
            json.dump(events_by_city, f, ensure_ascii=False, indent=4)
        print("Данные о мероприятиях успешно записаны в events.json.")
    else:
        print("Не удалось получить данные о мероприятиях из JSON-файла.")
