import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://cookpad.com"


def search_by_food(driver, food):
    driver.get(f"{URL}")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "keyword").send_keys(food)  # 検索にfoodの内容を入力
    driver.find_element(By.ID, "submit_button").click()  # 検索ボタンを押す
    # time.sleep(10)


def get_recipes(driver):
    pass


def main():
    food = 'トマト'

    # 前の方法
    # driver = webdriver.Chrome()
    # driver.get("")
    # driver.implicitly_wait(10)
    # driver.close()

    # withの方法(close忘れ防止)
    with webdriver.Chrome() as driver:
        search_by_food(driver, food)
        get_recipes(driver)


if __name__ == '__main__':
    main()
