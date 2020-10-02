from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


class TestGitHub:
    def test_Sample1(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Arun\\PycharmProjects\\SeleniumTest\\config\\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.maximize_window()
        data=driver.find_element_by_name("q")
        data.send_keys("chennai")
        data.send_keys(Keys.ENTER)



    def test_Sample2(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Arun\\PycharmProjects\\SeleniumTest\\config\\chromedriver.exe")
        driver.get("https://www.bing.com/")
        driver.maximize_window()
        data = driver.find_element_by_id("sb_form_q")
        data.send_keys("chennai")
        data.send_keys(Keys.ENTER)
        data = driver.find_element_by_id("sb_form_qaaa")