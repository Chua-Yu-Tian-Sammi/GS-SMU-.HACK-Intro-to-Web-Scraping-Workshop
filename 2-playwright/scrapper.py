import time
import os, json

from playwright.sync_api import sync_playwright
from datetime import datetime
from bs4 import BeautifulSoup

def extract_content_and_images(page, selector):
    # Get the HTML content of the element
    html = page.inner_html(selector)

    soup = BeautifulSoup(html, "html.parser")
    # Find all direct child divs (rows)
    rows = soup.find_all('div', recursive=False)
    contents = []
    for row in rows:
        # Each row contains multiple card divs (one per image/text block)
        cards = row.find_all('div', recursive=False)
        for card in cards:
            # Get all text inside the card (e.g., label under the image)
            text = card.get_text(separator=' ', strip=True)
            img = card.find('img')
            image_url = img['src'] if img else None
            contents.append({
                "text": text,
                "image": image_url
            })
    return contents

def save_scrapped(content):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Load existing data if present
    data = []
    if os.path.exists("scrapped.json"):
        with open("scrapped.json", "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception:
                data = []
    # Append new content
    if isinstance(content, list):
        for entry in content:
            data.append({
                "datetime": now,
                "text": entry["text"],
                "image": entry["image"]
            })
    else:
        data.append({
            "datetime": now,
            "text": content["text"],
            "image": content["image"]
        })
    # Save as JSON array
    with open("scrapped.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def login_and_scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Step 1: Go to login page
        page.goto("")  # TODO - To update with the actual URL of the login page

        # Step 2: Fill login form and submit
        page.fill('input[name="username"]', "heapuser")  # Use correct demo credentials
        page.fill('input[name="password"]', "password")

        time.sleep(3) # To show the login form before submitting
        page.click('button[type="submit"]')
        page.wait_for_load_state('domcontentloaded')

        # Step 3: Scrape initial content (each row in #content)
        initial_contents = extract_content_and_images(page, '#content')
        save_scrapped(initial_contents)

        # Step 4: Click "Load More" and scrape after each click
        for i in range(3):
            page.click('#load-more')
            time.sleep(2)  # Allow content to load

            # Scrape after each load more
            more_contents = extract_content_and_images(page, '#content')
            save_scrapped(more_contents)

        browser.close()

if __name__ == "__main__":
    login_and_scrape()
