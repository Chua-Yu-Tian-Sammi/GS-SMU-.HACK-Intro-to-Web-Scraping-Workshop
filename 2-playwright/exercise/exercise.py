from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # TODO: Load the local HTML file (adjust the path as needed)
    page.goto('http://localhost:8000/index.html')

    # TODO: Click the button to open the modal
    # page.click('...')

    # TODO: Wait for the modal to be visible
    # page.wait_for_selector('...')

    # TODO: Extract the text from the modal
    # modal_content = page.inner_text('...')

    # TODO: Print the modal content
    # print(modal_content)

    browser.close()
