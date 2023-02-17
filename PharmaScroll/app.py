import csv
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import *
import requests

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Initialize the web driver and go to the search page
driver = webdriver.Chrome()
#driver.set_page_load_timeout(60)
driver.get("https://search.medscape.com/search/")

# Read the search terms from a CSV file

reader = pd.read_excel("Name.xlsx")
entry = reader.columns[0]

def getAuthorData(link):
    # Execute JavaScript code to open a new tab
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    authors = []
    h3_tags = soup.find_all("h3")

    for tag in h3_tags[1:]:

        authors.append(tag)

    return authors


for row in reader[entry][:30]:
    # Find the search bar and enter the search term
    # search_bar = driver.find_element(By.CLASS_NAME,"searchInput")
    search_bar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "searchInput"))
    )

    search_bar.clear()
    search_bar.send_keys(row)
    search_bar.send_keys(Keys.RETURN)

    # Click on the "Advanced Search" button
    adSearch_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'profeducation')))
    adSearch_button.click()

    # advanced_search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'refineSearch')))
    # advanced_search_button.click()

    #     # Find the input field by name
    # input_field = driver.find_element(By.NAME,"age")

    # # Set the value of the input field
    # #input_field.send_keys("-1YEAR")
    # driver.execute_script("arguments[0].value = arguments[1];", input_field, "-1YEAR")

    res = []
    while True:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all the search results on the page
        search_results = soup.find_all('div', class_='searchResult')

        # Extract the relevant information from each search result
        for result in search_results:
            try:
                title = result.find('p', class_='searchResultTitle').text.strip()
                teaser = result.find('div', class_='searchResultTeaser').text.strip()
                info = result.find('p', class_='searchResultSources').text.strip().split(",")
                if info[-1] != " 2022":
                    continue
                date = ",".join(info[1:])
                
                
                p_tag = driver.find_element(By.CLASS_NAME, 'searchResultTitle')

                # Find the `a` tag within the `p` tag
                a_tag = p_tag.find_element(By.TAG_NAME, 'a')

                # Extract the `href` attribute value of the `a` tag
                link = a_tag.get_attribute('href')
                author = getAuthorData(link)
            except AttributeError or UnicodeEncodeError:
                continue

            # Print the information for each search result
            # print(f"Title: {title}")
            # print(f"Teaser: {teaser}")
            # print(f"Date: {date}")
            cur = [{
                "name":result,
                "date":date,
                "title":title,
                "summary":teaser,
                "url":link,
                "author":author

            }]
            res.append(cur)
        
        #Pagination
        next_button = soup.find('a', class_='pageNext')
        if next_button:
            # If there is a next page, click the button and continue the loop
            next_button.click()
        else:
            # If there is no next page, break out of the loop
            break
            
# Close the web driver
driver.quit()
df = pd.DataFrame(res)
output_file = 'my_output_file.csv'

# Save the DataFrame as a CSV file
df.to_csv(output_file, index=False)
