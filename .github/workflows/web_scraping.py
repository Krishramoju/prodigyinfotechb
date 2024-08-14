import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scraping():
    # URL of the e-commerce website (replace with the actual URL)
    url = 'https://example.com/products'
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lists to store the scraped data
    product_names = []
    product_prices = []
    product_ratings = []
    
    # Find the product elements (update the selectors based on the website's structure)
    for product in soup.find_all('div', class_='product'):
        name = product.find('h2', class_='product-name').text
        price = product.find('span', class_='product-price').text
        rating = product.find('span', class_='product-rating').text
        
        product_names.append(name)
        product_prices.append(price)
        product_ratings.append(rating)
    
    # Create a DataFrame
    data = {
        'Name': product_names,
        'Price': product_prices,
        'Rating': product_ratings
    }
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('products.csv', index=False)
    
    print("Data has been scraped and saved to products.csv")

if __name__ == "__main__":
    web_scraping()
