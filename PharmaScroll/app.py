import csv
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Initialize the web driver and go to the search page
driver = webdriver.Chrome()
driver.set_page_load_timeout(60)
driver.get("https://search.medscape.com/search/")

# Read the search terms from a CSV file

reader = pd.read_excel("Name.xlsx")
entry = reader.columns[0]
for row in reader[entry][:]:
    # Find the search bar and enter the search term
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "searchInput")))
    search_bar.clear()
    search_bar.send_keys(row)
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

        # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all the search results on the page
    search_results = soup.find_all('div', class_='searchResult')

        # Extract the relevant information from each search result
    for result in search_results:
        try:
            title = result.find('p', class_='searchResultTitle').text.strip()
            teaser = result.find('div', class_='searchResultTeaser').text.strip()
            date = result.find('p', class_='searchResultSources').text.strip()
        except AttributeError or UnicodeEncodeError:
            continue


        # Print the information for each search result
        print(f"Title: {title}")
        print(f"Teaser: {teaser}")
        print(f"Date: {date}")
        print()
            
# Close the web driver
driver.quit()
