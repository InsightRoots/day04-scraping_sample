def main():
    with open(file='users.txt', mode='r', encoding='utf-8') as f:
        # text = f.read()
        # #読み込むことができる
        # text = f.readlines()
        # # １行ごとに読み込む（改行してくれる）
        text = f.read().split('\n')  # 分かれるけど、最後にスペースが出来る。
    for user in text[:-1]:
        name, age = user.split(",")
        print(name, age, sep=":")
        # print(text)


if __name__ == '__main__':
    main()
