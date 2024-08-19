import requests
from bs4 import BeautifulSoup
import json
import random
import lorem


url = 'https://www.film.ru/a-z/movies'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

data = soup.find_all('div','redesign_afisha_movie_main')
cnt = 5

list_movies = []

for i in data:
    name = i.find("strong").text.strip()
    slug = i.find('span').text.strip().replace(' ','-')

    div = i.find('div', class_='redesign_afisha_movie_main_subtitle')
    year = div.find('span').next_sibling.strip()
    cnt +=1

    event = {
        "model": "main.movie",
        "pk": cnt,
        "fields": {
            "name": name,
            "slug": slug,
            "year": year,
            "during": random.randint(60, 180),
            "grade": random.randint(1, 10),
            "description": lorem.paragraph(),
            "category": random.randint(1,4)
        }
    }
    list_movies.append(event)


with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(list_movies, f, ensure_ascii=False, indent=4)

print("Данные успешно записаны в файл events.json")




import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import lxml
import random

list_events = []

url = "https://zakazbiletov.kz/en/events/5-shou"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

data = soup.find_all('article', 'event-item')
cnt = 86

for i in data:
    name = i.find("div",'event-item-title').text
    date = i.find('span','d-none d-sm-inline').text
    location = i.find("li", {"itemtype" : "http://schema.org/PostalAddress"}).text
    price = i.find("li", {"itemtype": "http://schema.org/Offer"},).find('span',{"itemprop": "price"} ).text
    price = price.replace(' ','')
    location  = location.strip()
    try:
        price = int(price)
    except:
        price = 2700

    print(f"INSERT INTO events (id, event_type, data, location,title,tickets_amount,ticket_price)")
    print(f"VALUES({cnt}, 'show', '{date}', '{location}', '{name}', {random.randint(1, 50)}, {price});")
    cnt +=1
for event_url in list_events:
    try:
        url = 'https://ticketon.kz/theatres'
        response = requests.get(event_url)
        event_soup = BeautifulSoup(response.text, "lxml")

        event_type = "theatre"
        name = event_soup.find("div",'_ontentDetails_title__NWpTc').text
        print(name)
        location = event_soup.find('p','AboutListItem_textContainer__ttk4m').text
        print(location)
        date = event_soup.find('span', 'AboutListItem_text__2aqVr').text
        print(date)
    except:
        continue

    date, price = event_soup.find('time').text.strip('.').split(",")
    new_price = 0

    location = ['Keruencity Astana', 'Eurasia Cinema', 'Chaplin MEGA Silk Way', 'Aru Cinema', 'Arman Asia Park', 'Saryarka KinoPark 8']

    amount_tickets = random.randint(1,50)

    for char in price:
        try:
            new_price = new_price * 10 + int(char)
        except:
            continue

    print(f"INSERT INTO events (id, event_type, data, location,title,tickets_amount,ticket_price)")
    print(f"VALUES({cnt}, '{event_type}', '{date}', '{random.choice(location)}', '{name}', {random.randint(1, 50)}, {new_price});")

    cnt += 1
    if(cnt == 66):
        break

for event_url in list_events:

    response = requests.get(event_url)
    event_soup = BeautifulSoup(response.text, "lxml")


    event_type = "movie"
    name = event_soup.find("h1").text
    date, price = event_soup.find('time').text.strip('.').split(",")
    new_price = 0

    location = ['Keruencity Astana', 'Eurasia Cinema', 'Chaplin MEGA Silk Way', 'Aru Cinema', 'Arman Asia Park', 'Saryarka KinoPark 8']

    amount_tickets = random.randint(1,50)

    for char in price:
        try:
            new_price = new_price * 10 + int(char)
        except:
            continue

    print(f"INSERT INTO events (id, event_type, data, location,title,tickets_amount,ticket_price)")
    print(f"VALUES({cnt}, '{event_type}', '{date}', '{random.choice(location)}', '{name}', {random.randint(1, 50)}, {new_price});")

    cnt += 1
    if(cnt == 34):
        break







