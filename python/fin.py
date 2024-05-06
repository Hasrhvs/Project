import requests
from bs4 import BeautifulSoup
import cx_Oracle

# Step 1: Set up the development environment
# Install the required libraries/packages: requests, BeautifulSoup, cx_Oracle

# Step 2: Extract data from the URL
url = "https://www.google.com/finance/quote/TCS:NSE"
response = requests.get(url)
html_content = response.content

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Step 3: Fill the form fields
# Assuming there are no form fields to fill

# Step 4: Extract the desired data
price = soup.find("div", class_="YMlKec fxKIJc").text
previous_close = soup.find("div", class_="rbb5Jf").text

# Step 5: Store the data in the Oracle database
# Connect to the Oracle database
connection = cx_Oracle.connect("HARSHVARDHANSINGH0210@GMAIL.COM", "Yash@1234", "hostname:port/ords/apex_admin")
cursor = connection.cursor()

# Create a table (if it doesn't exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_data (
        symbol VARCHAR(10),
        exchange VARCHAR(10),
        price NUMBER,
        previous_close NUMBER
    )
""")

# Insert the data into the table
symbol = "TCS"
exchange = "NSE"
cursor.execute("INSERT INTO stock_data (symbol, exchange, price, previous_close) VALUES (:1, :2, :3, :4)",
               (symbol, exchange, price, previous_close))

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Data stored successfully!")