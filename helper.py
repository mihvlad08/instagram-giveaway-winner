import credentials
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
action = ActionChains(driver)

class InstagramWinnerInterface:

    def __init__(self, giveawayURL, twoFA):
        self.twoFA = twoFA
        self.giveawayURL = giveawayURL

    def login(self):
        driver.get("https://www.instagram.com/")
        driver.maximize_window()

        cookie = driver.get_cookie('csrftoken')
        driver.add_cookie({"name": "csrftoken", "value": str(cookie)})

        accept_cookies = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        accept_cookies.click()

        login_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        login_input.send_keys(str(credentials.username))

        password_input = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password_input.send_keys(str(credentials.password))

        # This simulates submitting the form to a certain level
        password_input.send_keys(Keys.ENTER)

        if self.twoFA:
            driver.implicitly_wait(30)

        save_login_info = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        save_login_info.click()

        turn_on_notifications = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        turn_on_notifications.click()

    def goToGiveawayPost(self):
        driver.get(str(self.giveawayURL))

    def likePost(self):
        like_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
        time.sleep(5)
        like_button.click()

    def commentOnPost(self):
        return

