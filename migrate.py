import json
import sqlite3

with open('events.json', 'r', encoding='utf-8') as f:
    events_data = json.load(f)

conn = sqlite3.connect('./instance/db.sqlite')
cursor = conn.cursor()

for city, city_events in events_data.items():
    for event_title, event_info in city_events.items():
        title = event_info.get('title')
        description = event_info.get('description')
        category = event_info.get('category')
        image_url = event_info.get('image_url')
        event_url = event_info.get('url_to_event')
        cursor.execute('INSERT INTO events (title, decription, city, category, url_to_img, envent_url) VALUES (?, ?, ?, ?, ?, ?)',
                       (title, description, city, category, image_url, event_url))

conn.commit()
conn.close()

print('Data migrated successfully to SQLite database.')
