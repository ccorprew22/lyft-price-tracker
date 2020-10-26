from selenium import webdriver
import csv
import time
import re
import datetime
import os
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient


client = MongoClient() #Enter connection url from mongodb page


db = client[""] #Enter Database Name
collectionss = db[""] #Enter connection

def save_data_to_mongo(data):
    db = client[""] #Enter Database Name
    collection = db[""] #Enter connection
    collection.insert_one(data)

def scrape():
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5:'Saturday', 6:'Sunday'}
    site = 'https://ride.lyft.com/?entrypoint=lyftcom'
    path = '' #Enter path that contains chromedriver
    chrome_options = Options()
    chrome_options.add_argument("--headless") #Runs website traversal without opening chrome window
    driver = webdriver.Chrome(executable_path = path, options= chrome_options)

    url = driver.command_executor._url
    driver.get(site)

    pickup = driver.find_element_by_xpath("//input[@aria-label='Enter a pickup location']")
    destination = driver.find_element_by_xpath("//input[@aria-label='Enter a drop-off location']")

    #Enter in pickup and dropoff
    pickup.send_keys('') #Enter pickup address
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(), '')]").click() #Enter street address of pickup location in parathesis
    time.sleep(5)
    destination.send_keys('') #Enter destination address
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(text(), '')]").click() #xpath destination name is single parenthesis
    time.sleep(10)

    #Pick price range of driver package
    std_price = driver.find_element_by_id('standard-ride-button')

    n = datetime.datetime.now()
    
    t = n.strftime("%H:%M:%S")
    price_text = std_price.text
    price = re.search(r'\$.*', price_text).group()
    day_num = datetime.datetime.today().weekday()
    day = days[day_num]
    today = datetime.date.today()
    date = today.strftime("%B %d, %Y")
    time.sleep(2)

    driver.close()
    return [date, day, t, price]

i = 0
while True:
    
    lst = scrape()
    date = lst[0]
    day = lst[1]
    t = lst[2]
    price = lst[3]
    price = re.search(r'\$[0-9]*', price).group()
    data = {"_id": i, "date": date, "day": day, "time": time, "price": price}
    
    if os.path.isfile("lyft.csv") == True: #Enter path
        with open('lyft.csv', 'r+', newline='') as file:
            writer = csv.writer(file)
            reader = csv.reader(file)
            rows = list(reader)
            num = len(rows)-1
            #Gather first line number and add to it
            writer.writerow([int(rows[num][0])+1,date, day, t, price])
    else:
        with open('lyft.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["#","Date", "Day", "Time", "Price"])
            writer.writerow([0, date, day, t, price])
    save_data_to_mongo(data)
    i += 1
    time.sleep(60)
