import requests
from bs4 import BeautifulSoup
from icecream import ic
import pandas as pd
import json
import os


# Задание 1

def parcer() -> None:
    """
    Функция дря парсинга названия, ссылок, цен, информации об автомобилях Toyota Land Cruiser Prado с сайта av.by.
    (с учетом страниц). Сортирует автомобили по возрастанию цены.
    Выводит на экран полученые данные и количество автомобилей.
    Полученные данные функция записывает в файлы Land Cruiser Prado.xlsx и Land Cruiser Prado.json в текущей директории.
    :return: None
    """
    host: str = "https://cars.av.by"
    data: list = []
    for page in range(1, 4):
        print(f"Parsing page №:{page}.....")
        url: str = f"https://cars.av.by/filter?brands[0][brand]=1181&brands[0][model]=5731&page={page}"
        r = requests.get(url)
        if r.status_code == 200:
            print(f"Статус код: {r.status_code}")
            soup = BeautifulSoup(r.text, "html.parser")
            cars = soup.find_all("div", class_="listing-item")

            for car in cars:
                try:
                    model = car.find("div", class_="listing-item__about").find("h3").get_text().replace("\xa0", " "). \
                        replace("\u2009", " ")
                except Exception:
                    model = "-"

                try:
                    link = host + car.find("div", class_="listing-item__about").find("a").get("href")
                except:
                    link = "-"

                try:
                    price = car.find("div", class_="listing-item__prices").find("div", class_="listing-item__price"). \
                                get_text().replace("\xa0", " ").replace("\u2009", " ") + \
                            car.find("div", class_="listing-item__prices").find("div", class_="listing-item__priceusd"). \
                                get_text().replace("\xa0", " ").replace("\u2009", " ")
                except Exception:
                    price = "-"

                try:
                    info = car.find("div", class_="listing-item__params").get_text().replace("\xa0", " "). \
                        replace("\u2009", " ")
                except Exception:
                    info = "-"

                data.append([model, link, price, info])

    data.sort(key=lambda x: int(x[2].split()[0]))
    ic(data)
    print(f"Всего найдено {len(data)} автомобилей.")

    headers = ["Модель", "Ссылка", "Цена", "Информация"]
    df = pd.DataFrame(data, columns=headers)
    df.index += 1
    df.to_excel("Land Cruiser Prado.xlsx")

    with open("Land Cruiser Prado.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=3)


parcer()
print()


# Задание №2

def file_replace() -> None:
    """
    Функция запрашивает адрес директории для поиска формата файлов указаных пользователем
    и перемещает их в другую директорию, которую укажет пользователь.
    :return: None
    """
    location_1: str = input("Введите адрес директории для поиска: ")
    form: str = input("Введите формат файлов для перемещения (напр.: '.txt'): ")
    location_2: str = input("Введите адрес директории для перемещения туда файлов: ")
    counter: int = 0
    for file in os.listdir(location_1):
        if os.path.splitext(file)[1] == form:
            os.replace(location_1 + "\\" + file, location_2 + "\\" + file)
            print(f"Файл {file} из папки: {location_1}\ перемещен в папку: {location_2}\.")
            counter += 1
        else:
            pass
    print(f"Всего перемещено {counter} файлов.")


file_replace()
