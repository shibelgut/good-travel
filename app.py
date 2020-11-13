from flask import Flask, render_template  # подключаем модуль и render_template, который включает функции для Jinja
from data import tours, departures
import random

app = Flask(__name__)  # объявляем экземпляр flask


@app.route('/')
def index():
    # Создаем список случайных отелей
    list_random_items = [random.choice(list(tours.items()))]
    list_length = len(list_random_items)
    while list_length < 6:
        random_item_next = random.choice(list(tours.items()))
        count = 0
        for i in range(list_length):
            if list_random_items[i] != random_item_next:
                count += 1
        if count == list_length:
            list_random_items.append(random_item_next)
            list_length = len(list_random_items)

    list_numbers = []
    list_items = []
    for i in range(len(list_random_items)):
        lst = list(list_random_items[i])
        for j in range(len(lst)):
            if j % 2 == 0:
                list_numbers.append(lst[j])
            else:
                list_items.append(lst[j])

    # Получаем словарь случайно выбранных отелей
    random_tours = dict(zip(list_numbers, list_items))

    output = render_template('index.html', tours=random_tours, departure=departures)
    return output


@app.route('/departures/<name_departure>/')
def departure(name_departure):
    tours_departure = {}
    for key, value in tours.items():
        if value["departure"] == name_departure:
            tours_departure[key] = value
            destination = departures[name_departure]
    output = render_template('departure.html', destination=destination[3:], departure=departures, tours=tours_departure,
                             tours_list=list(tours_departure.values()))
    return output


@app.route('/tours/<int:id_tour>/')
def tours_id(id_tour):
    output = render_template('tour.html', tours=tours, departure=departures, id=id_tour)
    return output


if __name__ == '__main__':
    app.run()
