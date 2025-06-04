import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'
response = requests.get(url)

print("Status Code:", response.status_code)  # Debug

soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

print("Books Found:", len(books))  # Debug

book_list = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    book_list.append({'Title': title, 'Price': price})

df = pd.DataFrame(book_list)

print(df)  # Show the table

df.to_csv('books.csv', index=False)
print("✅ Data saved to books.csv")
