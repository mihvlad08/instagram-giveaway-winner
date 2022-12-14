import credentials
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
action = ActionChains(driver)

def login():

    driver.get("https://www.instagram.com/")
    driver.maximize_window()

    accept_cookies = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
    accept_cookies.click()

    login_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    login_input.send_keys(str(credentials.username))

    password_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    password_input.send_keys(str(credentials.password))

    password_input.send_keys(Keys.ENTER)
