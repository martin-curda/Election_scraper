"""
projekt_3.py: třetí projekt do Engeto Python Akademie

author: Martin Čurda
email: curda.mart@gmail.com
discord: Martin Č.#0010
"""
import requests
from bs4 import BeautifulSoup
import csv
import sys

base_url = "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=10&xobec="


def response_server(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def location(soup):
    city_names = soup.find_all("td", {"class": "overflow_name"})
    cities = [city.text for city in city_names]
    return cities


def codes(soup):
    city_codes = soup.find_all("td", {"class": "cislo"})
    code_text = [code.text for code in city_codes]
    return code_text


def parties(soup, code_text):
    for code in code_text:
        url = base_url + code
        soup = response_server(url)
        parties_name = soup.find_all("td", {"class": "overflow_name", "headers": ["t1sa1 t1sb2", "t2sa1 t2sb2"]})
        parties_text = [party.text for party in parties_name]
        return parties_text


def csv_table(parties_text, datas, file_name):
    fields = ['Code', 'Location', 'Registered', 'Envelopers', 'Valid'] + parties_text
    with open(file_name, 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, dialect="excel",)
        print(f"Ukládám data do {file_name}")
        writer.writeheader()
        for row in datas:
            writer.writerow(row)


def arguments():

    if len(sys.argv) != 3:
        print(f"Program potřebuje 2 argumenty! URL a složku csv. Ukončuji program.")
        sys.exit()

    if not sys.argv[1].startswith("https://www.volby.cz/pls/ps2017nss/"):
        print(f"První argument nebyl správně zadán. Ukončuji program.")
        sys.exit()

    if not sys.argv[2].endswith(".csv"):
        print(f"Druhý argument nebyl správně zadán. Ukončuji program.")
        sys.exit()

    else:
        print(f"Stahuji data z vybraného url: {sys.argv[1]} ")


def data(code_text, cities, parties_text):
    data_all = []
    for code, party in zip(code_text, cities):
        url = base_url + code
        soup = response_server(url)
        registered = int(soup.find("td", {"class": "cislo", "headers": "sa2"}).
                         text.replace(" ", "").replace('\xa0', ''))
        envelopers = int(soup.find("td", {"class": "cislo", "headers": "sa3"}).
                         text.replace(" ", "").replace('\xa0', ''))
        valid = int(soup.find("td", {"class": "cislo", "headers": "sa6"}).text.replace(" ", "").replace('\xa0', ''))
        votes = soup.find_all("td", {"class": "cislo", "headers": ["t1sa2 t1sb3", "t2sa2 t2sb3"]})
        votes_text = [vote.text.replace(" ", "").replace('\xa0', '') for vote in votes]

        row = {'Code': code, 'Location': party, 'Registered': registered, 'Envelopers': envelopers, 'Valid': valid}
        for partys, vote in zip(parties_text, votes_text):
            row[partys] = vote
        data_all.append(row)
    return data_all


def main():
    arguments()
    url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203"
    csv_file = "election_results.csv"
    soup = response_server(url)
    cities = location(soup)
    code_text = codes(soup)
    parties_text = parties(soup, code_text)
    data_main = data(code_text, cities, parties_text)
    csv_table(parties_text, data_main, csv_file)

    print(f"""Data byla uložena. Ukončuji program""")


if __name__ == '__main__':
    main()