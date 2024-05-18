from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(start_url)
#time.sleep(10)

scraped_data = []
stars_data = []

def scrape():

    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table = soup.find("table", attrs = {"class" : "wikitable"})
    table_body = bright_star_table.find("tbody")
    table_row = table_body.find_all("tr")

    for row in table_row:
        table_cols = row.find_all('td')
        print(table_cols)   

        temp_list = []

        for col in table_cols:
            data = col.text.strip()
            temp_list.append(data)

        scraped_data.append(temp_list)

for i in range(0, len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)
print(stars_data)

headers = ['Star_names', 'Distance', 'Mass', 'Radius', 'Lum']
star_df_1 = pd.DataFrame(stars_data, columns = headers)
star_df_1.to_csv('scraped_data.csv', index = True, index_label = "id")
