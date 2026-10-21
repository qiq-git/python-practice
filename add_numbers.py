while True:
    try:
        num1 = float(input("请输入一个数:"))
        num2 = float(input("请输入另一个数:"))
    except ValueError:
        print("请输入数字!")
        continue
    print(num1 + num2)


def my_sum(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return num1 + num2


print(my_sum(5, 6))
