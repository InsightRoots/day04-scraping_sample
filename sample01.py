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

from selenium.webdriver.common.keys import Keys


def main():
    food = "とまと"
    # ドライバーの立ち上げ(操作する人)
    driver = webdriver.Chrome()
    # Googleにアクセスする.getがアクセスするコード
    driver.get("https://www.google.co.jp/")

    # driverで取得してきた。その中から、さらに入力して取得していく
    # ID要素に対して、入力したことを渡す↓
    driver.find_element(By.NAME, "q").send_keys(food)
    # Byにも色々あるので、このセレニウムの中にある、By
    # Byってなんだ？ByNAMEってなんだ？そこに"q"を渡している、ということ
    driver.find_element("name", "q").send_keys(Keys.ENTER)

    time.sleep(2)
    driver.close()
    # 開いたら、閉じる、という形にする。なぜなら、キャッシュ（まだ使うよね）という認識で、どんどん積もっていってしまう。

    # グーグルにアクセスする


if __name__ == '__main__':
    main()
