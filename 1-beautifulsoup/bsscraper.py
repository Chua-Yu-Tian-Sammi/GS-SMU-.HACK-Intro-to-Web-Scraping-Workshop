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
# TODO: fill in the relevant attributes to filter
    # hint: use get_text()

# titles = soup.find_all(...)

# CHALLENGE 2: Structured Pairing
# TODO: fill in the relevant attributes, print using this format: print(f"{title} - {price}")

# books = soup.find_all(...)


# CHALLENGE 3: Conditional Filtering
# TODO: conditionally print "In stock" books, print using this format: print(f"{title} ({stock})")

# for book in books:
#     stock = book.find(...).get_text()


# CHALLENGE 4: Data Aggregation & Comparison -- find books with highest price
# TODO: fill in the relevant attributes and add some logic to compare the prices

# top_books = []
# max_price = 0.0

# for book in books:
#     price_text = book.find(...).get_text()
#     price = float(price_text.strip('$'))  # Convert "$14.99" to 14.99

# for title, price in top_books:
#     print(f"{title} - ${price:.2f}")
