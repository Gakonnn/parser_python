import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import lxml
import random

list_events = []

url = "https://ticketon.kz/theatres"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

data = soup.find_all('div', 'block-1 list-block')

for i in data:
    event_url = "https://ticketon.kz"+ i.find('a').get('href')
    list_events.append(event_url)

dict = defaultdict()
cnt = 33

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







