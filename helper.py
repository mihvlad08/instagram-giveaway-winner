import credentials
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
action = ActionChains(driver)

class InstagramWinnerInterface:

    def __init__(self, giveawayURL, twoFA):
        self.twoFA = twoFA
        self.giveawayURL = giveawayURL

    def login(self):
        driver.get("https://www.instagram.com/")
        driver.add_cookie({"name": "csrftoken", "value": "3T5swQiwY5ndMhhb8qbuNLybdxvfmzGg"})
        driver.maximize_window()

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

    def goToGiveawayPost(self):
        return

    def likePost(self):
        return

    def commentOnPost(self):
        return

