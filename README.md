
# Find event

Это приложение, которое поможет вам найти события в вашем городе!



## Установка

Чтобы установить этот проект:

```bash
  git clone https://github.com/DWDW2/nfac_app.git
```
Далее вам нужно установить виртуальное окружение языка программирования python и активировать его.
```bash
python -m venv env 
/////////////////// после установки виртуального окружения
env\scripts\activate
```
```bash
pip install -r requirments.txt
```
и наконец: 
```bash
python migrate.py
flask run
```



если вам будет лень читать мой отчет о приложении, то коротко:


## Проблемы
- Регестрация и ауентификация есть, но она бесполезна т.к нету страницы профиля 
- Отсутсвие внешних приложений(Google calendar)
- Google oauth - я не знал как работать. Потратил много времени

## Решения 
- Уделить время чтению документации google oauth 2.0
- Изучить как создавать хорошую архетиктуру для сайта 
- Добавить в архитектуру более продвинутые технологии (кэширование, более функциональная субд и т.п)
## Технологии

**Client:** HTML, CSS, Bootstrap

**Server:** Sqlite, Flask, SQLalchemy

**Other:** BeautifulSoup4 

Я использовал простую но удобную библеотеку для того чтобы создать динамичное приложение - FLask. С библеотекой проблем не было, однако, моя неопытность давала о себе знать: были проблемы с маршрутизацией. Также я использовал sqlite - это СУБД, которая запускается локально на компьютере и от туда берет все данные. 
Главной проблемой было то, что я хотел реализовать добавление в гугл календарь и потратил слишком много времени впустую пытаясь решить проблемы с google API. Вы можете увидеть у меня в проекте ветку "google_account". В этой ветке я попытался реализовать Логин/Регестрацию через oauthlib, к сожалению у меня не получилось. На данный момент приложение может читать данные с базы, и искать совпадения с запросами пользователей. Также я использовал парсер от BeautifulSoup4 для того чтобы получить информацию о событиях в городах и всю информацию я созранил в json файле. Однако, я считаю, что можно было это сделать лучше, если бы кто-нибудь предостовлял API для получения информации о событиях, но такого к сожалению нету. Я добавил систему регестрации и ауентификации с испольованием хэширования, но эта функция бесполезна т.к я не успел сделать страницу профиля где отображались бы зарегестрированные мероприятия. 
## Что я хочу сделать в будущем?
Я хочу исправить фронт сайта для того чтобы сделать приложение юзер-френдли. Также я планирую изучить документацию о google oauth 2.0 для того чтобы можно было добавлять информацию в гугл календарь и другие полезные вещи, которые дает нам google. Также я планирую изучить то как создать хорошую архитектуру, добавив туда более большие и мощные инструменты.

## Nfactorial 
Это мой проект. Спасибо, что изучили и прочитали это README.md файл. 
