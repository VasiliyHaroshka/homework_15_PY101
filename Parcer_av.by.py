import requests
from bs4 import BeautifulSoup
from icecream import ic
import pandas as pd
import json


def parcer() -> None:
    """
    Function for parcins models, links, prices and other common information about cars Toyota Land Cruiser Prado from
    site 'av.by'. This parcer suppurts multipages.
    Results of parcing will be shown with ascend of prices.
    Function creates files Land Cruiser Prado.xlsx and Land Cruiser Prado.json in local directory for record of results.
    :return: None
    """
    host: str = "https://cars.av.by"
    data: list = []
    for page in range(1, 4):
        print(f"Parsing page №:{page}.....")
        url: str = f"https://cars.av.by/filter?brands[0][brand]=1181&brands[0][model]=5731&page={page}"
        r = requests.get(url)
        if r.status_code == 200:
            print(f"Status code: {r.status_code}")
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
                except Exception:
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
    print(f"{len(data)} results have been found.")

    headers = ["Model", "Link", "Price", "Common information"]
    df = pd.DataFrame(data, columns=headers)
    df.index += 1
    df.to_excel("Land Cruiser Prado.xlsx")

    with open("Land Cruiser Prado.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=3)


parcer()



