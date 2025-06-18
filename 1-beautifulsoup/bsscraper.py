import requests
from bs4 import BeautifulSoup

# Step 1: Place the URL & Access its contents
URL = "https://beautiful-soup-workshop.vercel.app/"

## For "not accepted" error: add user agent (can find your user agent here: https://www.whatismyip.com/user-agent/ 
#                                            -> replace it in the header)
# headers = {
#     'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
# }

response = requests.get(URL)
print(response.content)

# Step 2: Create BeautifulSoup object
soup = BeautifulSoup(response.content, "html5lib")

# Step 3: Analyse the parse tree
print("\n--- Prettified HTML snippet ---\n")
print(soup.prettify()) # this prints the raw HTML
print("\n--- End snippet ---\n")

# CHALLENGE 1: Extract all book titles
titles = soup.find_all("h2", class_="book-title")
for title in titles:
    print(title.get_text())

# CHALLENGE 2: Structured Pairing
books = soup.find_all("div", class_="book-card")
for book in books:
    title = book.find("h2", class_="book-title").get_text()
    price = book.find("p", class_="price").get_text()
    print(f"{title} - {price}")

# CHALLENGE 3: Conditional Filtering
books = soup.find_all("div", class_="book-card")
for book in books:
    stock = book.find("p", class_="stock").get_text()
    if "In stock" in stock:
        title = book.find("h2", class_="book-title").get_text()
        print(f"{title} ({stock})")

# CHALLENGE 4: Data Aggregation & Comparison -- find books with highest price
top_books = []
max_price = 0.0

for book in books:
    title = book.find("h2", class_="book-title").get_text()
    price_text = book.find("p", class_="price").get_text()
    price = float(price_text.strip('$'))  # Convert "$14.99" to 14.99

    if price > max_price:
        max_price = price
        top_books = [(title, price)]
    elif price == max_price:
        top_books.append((title, price))

for title, price in top_books:
    print(f"{title} - ${price:.2f}")
