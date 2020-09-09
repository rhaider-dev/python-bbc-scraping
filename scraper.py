import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.bbc.com/news'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='news-top-stories-container')
#print(results.prettify())

summary_all=results.find_all('p', class_='gs-c-promo-summary')

with open('summary.csv', mode='w') as summary_file:
    summary_writer = csv.writer(summary_file, quoting=csv.QUOTE_MINIMAL)
    summary_writer.writerow(['Summary'])

    for summary in summary_all:
        print(summary.text)
        # writing in csv
        summary_writer.writerow([summary.text])
