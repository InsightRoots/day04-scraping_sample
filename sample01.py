# セレニウムの中の　ウェブドライバーを出してくる
# インタープリターでセレニウムをダウンロード

from selenium import webdriver
# noinspection PyUnresolvedReferences
# グレーアウト部分をAlt＋エンターにして、インポートの最適化、ステートメントを抑止（つまり、このグレーアウトを無視する）
import chromedriver_binary


# グレーアウトでOK。webdriver.chromeの中で、これが動いているイメージ。chromedriver


def main():
    food = "とまと"
    # ドライバーの立ち上げ(操作する人)
    driver = webdriver.chrome()

    # グーグルにアクセスする


if __name__ == '__main__':
    main()
