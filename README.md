# python-practice

我的 Python 练习仓库。2026 年 10 月开始系统学 Python，这里放**我自己写的**程序——不是照着教程抄的，是写崩过、自己修好的。

## 目录

| 文件 | 是什么 | 用到的语法 |
|---|---|---|
| `guess_number.py` | 猜数字小游戏：随机 1–100，提示「大了 / 小了」，猜中报次数 | `random` / `while` / `if-elif-else` / `try-except` |
| `add_numbers.py` | 两个数相加，支持小数，输入非法不崩 | `float()` / `input()` / `while` / `try-except` / 函数 |

## 运行

需要 Python 3.10+（我用的是 3.14）。

```bash
python guess_number.py
python add_numbers.py
```

## 我踩过的坑

1. **`int(input())` 遇到字母会直接崩。** `input()` 拿到的是字符串，转数字失败时 `int()` 抛 `ValueError`，程序整个退出。用 `try / except ValueError` 接住，提示「请输入一个整数」再 `continue` 回到循环。
2. **加 `try` 的时候忘了删掉原来那行 `input()`。** 结果程序问两遍，而且还照样崩。教训：改代码是**替换**，不是往后追加。
3. **大小比较写反过。** 秘密数比猜的数大，说明是「猜小了」。这种错光看代码看不出来，自己玩一局立刻暴露。

## 下一步

- 把重复的「输入 → 转数字 → 出错重来」抽成一个函数（`add_numbers.py` 里已经开始试着写 `my_sum()`）
- 学完文件读写后，把每局战绩存到本地
