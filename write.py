def main():
    f = open(file='users.txt', mode='w', encoding='utf-8')
    # 対象ファイルに、書き方、文字コードをこれに決めようよ。
    # mode を変えることで、結果がかわる　。modeは常に上書き。aはアド、Add（横につながる）
    f.write('Bob,79')
    # 書き込むのはこれだよ
    f.close()
    #     開けたら閉めるのルールだから書いてある。→締め忘れ防止の方法が適用できる。つまり、With as
    with open(file='users.txt', mode='a', encoding='utf-8') as f:
        f.write('Bob,79\n')
        f.write('Tom,59\n')
        print("withの中:", f.closed)
    print("withの外:", f.closed)
    # Pythonはインデントが重要


if __name__ == '__main__':
    main()
