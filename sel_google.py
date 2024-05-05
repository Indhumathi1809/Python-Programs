from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome web driver (you can use other drivers like Firefox or Edge)
driver = webdriver.Chrome()

try:
    # Open a website
    driver.get("https://www.google.com")

    # Find the search input element by its name attribute
    search_input = driver.find_element_by_name("q")

    # Type a search query into the input element
    search_input.send_keys("Python programming")

    # Simulate pressing the Enter key to perform the search
    search_input.send_keys(Keys.ENTER)

    # Wait for a few seconds to let the search results load
    time.sleep(3)

    # Get the search results
    search_results = driver.find_elements_by_css_selector("h3")

    # Print the titles of the search results
    for result in search_results:
        print(result.text)

finally:
    # Close the browser window
    driver.quit()
