from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#sqlite3 imports
import sqlite3

#time import
import time

driver = webdriver.Chrome()
driver.maximize_window()

#connect to db
conn = sqlite3.connect('jobslinks.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY, link TEXT)')

#insert into db



def test():
    try: 
        driver.get("https://www.fuzu.com/login")
    except Exception as e:
        print('Not Working because of: ', e)

test()


def login_credentials():
    try:
        email_field = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/div[2]/div/form/div[1]/div/input[@type="email"]')
        password_field = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/div[2]/div/form/div[2]/div/input[@type="password"]')
        enabled_button = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/div[2]/div/form/button')
        if email_field and password_field:
            email_field.send_keys('mugaojoy@gmail.com')
            password_field.send_keys('_4hij7#SmXUrsd8')
            enabled_button.click()
            time.sleep(5)
            go_to_jobs()
            get_apply_link()

    except Exception as e:
        print('Not Working because of: ', e)

def go_to_jobs():
    driver.get('https://www.fuzu.com/jobs')
    time.sleep(5)
    search_bar = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/main/div[1]/div[1]/div/input')
    search_bar.send_keys('software engineer')
    search_bar.send_keys(Keys.ENTER)
    time.sleep(5)
    apply_button = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/main/div/section[2]/div[1]/div[2]/div[3]/div/a/span')
    apply_button.click()
    time.sleep(10)

def get_apply_link():
    apply_link = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/main/div[5]/div/a')
    apply_href = apply_link.get_attribute('href')
    cursor.execute('INSERT INTO links VALUES(?,?)', (1, apply_href))
    conn.commit()
    print(apply_href)


login_credentials()
cursor.close()

#action chains to apply more than one job- create a repetitive process