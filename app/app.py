import json
import concurrent.futures
import requests
from bs4 import BeautifulSoup
from database_writer import database_writer


BASE_URL = 'https://books.toscrape.com/catalogue/'


def get_book_data(book_url):
    """Get book data from book url.
    
    Args:
        book_url (str): Book url.
        
    Returns:
        dict: Book data.
    """
    response = requests.get(book_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('h1').text
    #upc = soup.find('th', string='UPC').find_next_sibling('td').text
    upc_element = soup.find('th', string='UPC')
    upc = upc_element.find_next_sibling('td').text if upc_element else 'No UPC'
    category_elements = soup.find('ul', class_='breadcrumb').find_all('a')
    category = category_elements[2].text.strip() if len(category_elements) > 2 else 'No Category'
    price = soup.find('p', class_='price_color').text[2:]
    stock = soup.find('p', class_='instock availability').text.strip().split('(')[1].split(' ')[0]
    rating = soup.find('p', class_='star-rating')['class'][1]
    rating_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    rating_value = rating_dict.get(rating, 0)
    
    dict_book = {
        'Title': title,
        'UPC': upc,
        'Category': category,
        'Price (GBP)': price,
        'Stock': stock,
        'Rating': rating_value
    }
    print(f"Dict Book: {dict_book}")
    
    return dict_book
    

def scrape_all_books(url):
    books = []
    urls_to_scrape = [url]

    while urls_to_scrape:
        current_url = urls_to_scrape.pop(0)
        print(f"Processando atualmente a seguinte URL: {current_url}")
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        book_links = [BASE_URL + x['href'] for x in soup.select('h3 > a')]
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            books.extend(list(executor.map(get_book_data, book_links)))

        next_button = soup.find('li', class_='next')
        if next_button:
            next_page_url = 'https://books.toscrape.com/catalogue/' + next_button.a['href']
            urls_to_scrape.append(next_page_url)

    return books


all_books = scrape_all_books("https://books.toscrape.com/catalogue/page-1.html")
filename = 'books_toscrape.json'

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_books, f, ensure_ascii=False, indent=4)
    

database_writer()