import requests
from bs4 import BeautifulSoup


def feeds_from_file(filename):
    data = ""
    with open(filename, 'r') as read_file:
        return read_file.readlines()


for feed in feeds_from_file('feeds.txt'):
    try:
        res = requests.get(feed, verify=False)

        if res.status_code == 404:
            continue

        soup = BeautifulSoup(res.text, 'html.parser')
        print(soup.titleline)
    except:
        continue
