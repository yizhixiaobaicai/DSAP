# _*_ coding: utf-8 _*_
# @File Name: fraction.py
# @Time: 2024/6/11 20:07
# @Author: Dongdong
# @E-mail Address: 1141305121@qq.com

def gcd(m, n):  # 计算m,n的最大公因数,采用欧几里得算法
    while True:
        remainder = m%n
        if remainder == 0:
            return n
        else:
            m = n
            n = remainder

class Fraction:
    def __init__(self, top, bottom):
        self.num = top  # 分子
        self.den = bottom  # 分母

    def __str__(self):  # 对方法进重写
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):  # 对加法进行重写
        num = self.num*other.den+self.den*other.num
        den = self.den*other.den
        a = gcd(num, den)  # 计算最大公因数
        return Fraction(num//a, den//a)

    def __eq__(self, other):  # 对相等的方法进行重写
        firstnum = self.num*other.den
        secondnum = self.den*other.num

        return firstnum == secondnum


if __name__ == "__main__":
    fra1 = Fraction(5, 10)
    fra2 = Fraction(3, 5)
    print(fra1==fra2)
