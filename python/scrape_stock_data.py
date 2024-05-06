import requests
from bs4 import BeautifulSoup
import re
import psycopg2

def scrape_stock_data(symbol, exchange):
    url = f"https://www.google.com/finance/quote/{symbol}:{exchange}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting data
    price_element = soup.find("div", class_="YMlKec fxKbKc")
    prev_close_element = soup.find("div", class_="P6K39c")
    
    if price_element and prev_close_element:
        price = price_element.text
        prev_close = prev_close_element.text
        
        # Clean up the data
        price = re.sub(r'[^\d.]', '', price)  # Remove non-numeric characters except '.'
        prev_close = re.sub(r'[^\d.]', '', prev_close)
        
        return {
            "price": float(price),  # Convert to float
            "previous_close": float(prev_close)
        }
    else:
        return None

def insert_stock_data(symbol, exchange, price, previous_close):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="yASH@1234",
            host="localhost"
        )
        cursor = connection.cursor()
        
        cursor.execute("""
            INSERT INTO stock_data (symbol_code, exchange, price, previous_close)
            VALUES (%s, %s, %s, %s)
        """, (symbol, exchange, price, previous_close))
        
        connection.commit()
        print("Data inserted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data into PostgreSQL:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

symbol = "RELIANCE"
exchange = "NSE"

data = scrape_stock_data(symbol, exchange)
if data:
    insert_stock_data(symbol, exchange, data['price'], data['previous_close'])
else:
    print("Failed to scrape data. Please verify the class names.")

from bs4 import BeautifulSoup
import re
import psycopg2

def scrape_stock_data(symbol, exchange):
    url = f"https://www.google.com/finance/quote/{symbol}:{exchange}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting data
    price_element = soup.find("div", class_="YMlKec fxKbKc")
    prev_close_element = soup.find("div", class_="P6K39c")
    
    if price_element and prev_close_element:
        price = price_element.text
        prev_close = prev_close_element.text
        
        # Clean up the data
        price = re.sub(r'[^\d.]', '', price)  # Remove non-numeric characters except '.'
        prev_close = re.sub(r'[^\d.]', '', prev_close)
        
        return {
            "price": float(price),  # Convert to float
            "previous_close": float(prev_close)
        }
    else:
        return None

def insert_stock_data(symbol, exchange, price, previous_close):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="yASH@1234",
            host="localhost"
        )
        cursor = connection.cursor()
        
        cursor.execute("""
            INSERT INTO stock_data (symbol_code, exchange, price, previous_close)
            VALUES (%s, %s, %s, %s)
        """, (symbol, exchange, price, previous_close))
        
        connection.commit()
        print("Data inserted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data into PostgreSQL:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

symbol = "RELIANCE"
exchange = "NSE"

data = scrape_stock_data(symbol, exchange)
if data:
    insert_stock_data(symbol, exchange, data['price'], data['previous_close'])
else:
    print("Failed to scrape data. Please verify the class names.")
