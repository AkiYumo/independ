

while True:
    input_n = input("数字を入力してください：")

    if input_n == "q":
        print("終了します")
        break



    try:
        n = int(input_n)
        if input_n == "1":
            print("正解")
            break
        else:
            print("不正解")
            

    except(ValueError):
        print("数字を入力するかqで終了します。")
        
