import json
import requests
from tqdm import tqdm

URL = 'https://en.wikipedia.org/wiki/'


class WikiPage:
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        with open(self.file, 'r', encoding="UTf-8") as file:
            countries = json.load(file)

        country_list = []
        for name in countries:
            country_list.append(name['name']['common'])
        self.country = iter(country_list)
        return self

    def __next__(self):
        country = next(self.country)

        with requests.Session() as s:
            resp = s.get(URL + country)
            if resp.status_code != 200:
                raise StopIteration

        return f'{country}, {URL + country}\n'


if __name__ == '__main__':
    for c in tqdm(WikiPage('countries.json')):
        with open('links.txt', 'a', encoding="UTf-8") as f:
            f.write(c)
