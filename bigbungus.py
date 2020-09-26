import requests
import json
import time
from random import choice

TOKEN = "1115297640:AAGBHOTaM12GHRwc5YqHtjenvkbjo6edp4c"
URL = "https://api.telegram.org/bot{token}/{method}"
id_set = None
quotes = None

def quote_lst():
    q = open("quotes.txt", "r")
    quotes_loc = [line.strip() for line in q if line.strip() != '']
    q.close()
    return quotes_loc

def send(id, text):
    data = {
        "chat_id": id,
        "text": text
    }
    p = requests.post(URL.format(token=TOKEN, method="sendMessage"), data=data)


def main():
    g = requests.get(URL.format(token=TOKEN, method="getUpdates"))
    g = g.json()

    for update in g["result"]:
        if update["update_id"] in id_set or "message" not in update:
            continue
        sender_id = update["message"]["chat"]["id"]
        txt = choice(quotes)
        send(sender_id, txt)
        id_set.add(update["update_id"])


def read_data():
    id_file = open('idfile.txt', 'r')
    id_gen = (int(line.strip()) for line in id_file)
    id_set_loc = set(id_gen)
    id_file.close()
    return id_set_loc

#change

def save_data():
    id_file = open('idfile.txt', 'w')
    for item in id_set:
        id_file.write(f'{item}\n')
    id_file.close()

quotes = quote_lst()
id_set = read_data()

try:
    while True:
        time.sleep(2)
        main()

except KeyboardInterrupt:
    save_data()
