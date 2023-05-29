import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv


payloads = {'trending': 'forever', 'page': 1}
url = 'https://openlibrary.org/trending/forever'
h = {'Accept-Language': 'en-US'}
file = open('books.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
# csv_obj.writerow(['Title', 'Author', 'AmountOfEditions'])


while payloads['page'] < 6:
    response = requests.get(url, params=payloads, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    books_soup = soup.find('div', class_='mybooks-list')
    all_books = books_soup.find_all('div', class_='details')
    for book in all_books:
        title = book.h3.a.text
        author=book.span.a.text
        amountofeditions = book.find('span', class_='resultPublisher').a.text
        print(title, author, amountofeditions)
        csv_obj.writerow([title, author, amountofeditions])
    payloads['page'] += 1
    sleep(randint(15, 20))