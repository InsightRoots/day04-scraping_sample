# セレニウムの中の　ウェブドライバーを出してくる
# インタープリターでセレニウムをダウンロード

import time

from selenium import webdriver
# noinspection PyUnresolvedReferences
# グレーアウト部分をAlt＋エンターにして、インポートの最適化、ステートメントを抑止（つまり、このグレーアウトを無視する）
import chromedriver_binary

from selenium.webdriver.common.by import By
# Byにも色々あるので、このセレニウムの中にある、By
# グレーアウトでOK。webdriver.chromeの中で、これが動いているイメージ。chromedriver

# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys

URL = "https://cookpad.com"


def search_by_food(driver, food):
    # ここにフードが入っていないので、入れてあげる
    driver.get(f"{URL}")
    driver.implicitly_wait(10)
    #  このままだと、アクセスして、10秒で閉じる、ということ
    #     検索にフードの内容を入力
    driver.find_element(By.ID, "keyword").send_keys(food)
    # 検索ボタンを押す
    driver.find_element(By.ID, "submit_button").click()
    # time.sleep(10)


def get_recipes(driver):
    recipe_previews = driver.find_elements(By.CLASS_NAME, "recipe-preview")
    # print(recipe_previews)

    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").text
        recipe_url = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").get_attribute('href')
        # recipes.append()
        # print(recipe_title, recipe_url)
        recipes.append(
            {"title": recipe_title,
             "url": recipe_url})
    return recipes


def main():
    food = "角煮"
    # ドライバーを準備して、閉める、という一連の流れ。
    # """""
    # # 前の方法
    # webdriver = webdriver.Chrome()
    # driver.get("")
    # driver.impactly_wait(10)
    # driver.close()

    # """
    # withの方法(close忘れ防止方法。Withにいる間は開いているが、そこから出たら閉じる、という方法)
    with webdriver.Chrome() as driver:
        search_by_food(driver, food)
        recipes = get_recipes(driver)

        for recipe in recipes:
            print(f"レシピ名 {recipe['title']}, URL:{recipe['url']}")


if __name__ == '__main__':
    main()
