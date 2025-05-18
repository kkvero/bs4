# Скрипт для первых 20 страниц википедии

import csv
import re
import time

import requests
from bs4 import BeautifulSoup

base_url = "https://ru.wikipedia.org"
category_url = "/wiki/Категория:Животные_по_алфавиту"
start_page = base_url + category_url

animals_dict = {}  # {'letter': count, ..}


def count_animals_on_page(url):
    """
    Посчитать имена животных на странице с данным url. Записать в animals_dict.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # entries = soup.select(".mw-category-group ul li") # будет включать раздел Подкатегории
    groups_all = soup.select(".mw-category-group")
    # Не включать раздел Подкатегории: Знаменитые животные по алфавиту, Породы по алфавиту
    groups_letters = groups_all[2:]
    entries = []
    for group in groups_letters:
        entries += group.select("ul li")

    animal_names = [entry.get_text(strip=True) for entry in entries]
    for animal in animal_names:
        animals_dict[animal[0]] = animals_dict.get(animal[0], 0) + 1
    # print(len(animal_names), animals_dict)


def get_next_page(url):
    """
    На данном url найти url следующей страницы.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    next_page_node = soup.find(string=re.compile(r"\b(Следующая страница)\b"))
    parent = next_page_node.parent
    next_page_url = None
    if parent.name == "a" and parent.has_attr("href"):
        next_page_url = parent["href"]
    return next_page_url


def main():
    url = start_page
    loop = 0
    while url and loop <= 20:
        count_animals_on_page(url)
        url_end = get_next_page(url)
        url = base_url + url_end
        time.sleep(0.5)  # чтобы не перегружать сервер
        loop += 1

    with open("beasts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter, count in animals_dict.items():
            writer.writerow([letter, count])
    print("Готово. Результат в файле beasts.csv.")


if __name__ == "__main__":
    main()
