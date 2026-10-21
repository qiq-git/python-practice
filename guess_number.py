import random

secret = random.randint(1, 100)   # 随机整数 1-100
count = 0

while True:
    try:
        guess = int(input("请输入你猜的数字:"))   # 防止输入非数字导致程序崩溃
        count = count + 1
    except ValueError:
        print("请输入一个整数")
        continue

    if secret > guess:
        print("猜小了!")
    elif secret < guess:
        print("猜大了!")
    else:
        print("恭喜您,猜对了!")
        break

print("您猜的次数为:", count)
