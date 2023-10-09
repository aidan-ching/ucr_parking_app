import os
from twilio.rest import Client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time

load_dotenv()

def update_spaces():
    driver = webdriver.Chrome()
    driver.get("https://lotspaces.ucr.edu/home")
    big_springs_one = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][1]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )

    big_springs_two = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][2]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )

    lot_six = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][3]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )

    lot_twenty_four = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][4]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )

    lot_twenty_six = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][5]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )

    lot_thirty = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][6]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )

    lot_fifty = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][8]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )

    lot_thirty_two = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-ucr-app/div[@id='main-content']/mat-sidenav-container[@class='mat-drawer-container mat-sidenav-container']/mat-sidenav-content[@class='mat-drawer-content mat-sidenav-content ng-star-inserted']/main/app-lot-spaces[@class='ng-star-inserted']/div[@class='row'][2]/div[@class='small-12 medium-6 column ng-star-inserted'][7]/mat-card[@class='mat-card mat-focus-indicator lot-card width-100']/mat-card-content[@class='mat-card-content']/div[@class='progress']"))
    )
    #lets parse the data that we have gathered
    info = [("Big Springs 1", big_springs_one.text.split("\n")), ("Big Springs 2", big_springs_two.text.split("\n")), ("Lot 6", lot_six.text.split("\n")),
                    ("Lot 24", lot_twenty_four.text.split("\n")), ("Lot 26", lot_twenty_six.text.split("\n")), ("Lot 30", lot_thirty.text.split("\n")),
                    ("Lot 32", lot_thirty_two.text.split("\n")), ("Lot 50", lot_fifty.text.split("\n")),]
    
    for lot in info:
        lot[1][0] = int(lot[1][0][:-1])
    
    #info[n][0] -> percentage of lot full (int)
    #info[n][1] -> taken spaces/all spaces (string)
    driver.quit()

    return info

def send_message(message, number): 
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    send_from = os.getenv('TWILIO_FROM_NUMBER')

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message,
            from_=send_from,
            to=number
        )
    print(message.sid)


#0 -> big springs 1
#1 -> big springs 2
#2 -> lot 6
#3 -> lot 24
#4 -> lot 26
#5 -> lot 30
#6 -> lot 32
#7 -> lot 50

alert_for = [5,6]
threshold = 90 #percentage to alert
number = "+1" # put number in here

try:
    while True:
        info = update_spaces()
        message = ''
        for i in range(len(info)):
            if info[i][1][0] >= threshold and i in alert_for:
                message += info[i][0] + " is at " + str(info[i][1][0]) + "% capacity\n" 
        if message != '':
            send_message(message, number)
            print("Message sent!")
        else:
            print("No lots above threshold")
        time.sleep(1800)
except KeyboardInterrupt:
    pass