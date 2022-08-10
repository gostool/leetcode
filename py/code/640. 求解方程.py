#!/usr/bin/env python

class Solution:
    def compute(self, exp: str):
        """

        :param exp:
        :return: n*x + c
        """
        x_n = 0
        # 处理x开头
        if exp[0] == "x":
            x_n = 1
            exp = exp[1:]
        # 处理-x
        if exp[0:2] == "-x":
            x_n = -1
            exp = exp[2:]
        n1 = exp.count("-x")
        n2 = exp.count("+x")
        exp = exp.replace("-x", "-1", n1)
        exp = exp.replace("+x", "+1", n2)
        print("exp:", exp, n1, n2)
        if exp != "":
            ret = eval(exp)
        else:
            ret = 0
        data = {
            'x': x_n + (n2-n1),
            'c': ret-(n1*-1)-(n2*1),
        }
        print("x_n:{} exp:{} data:{}".format(x_n, exp, data))
        return data

    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        # 规整
        # print(left, right)
        left_map = self.compute(left)
        right_map = self.compute(right)
        # 合并左右. n*x = c
        n = left_map['x'] - right_map['x']
        c = right_map['c'] - left_map['c']
        print("{}*x={}".format(n, c))
        # 计算x
        if n == 0:
            return "Infinite solutions"
        x = int(c/n)
        return "x={}".format(x)


def main():
    # equation = "x+5-3+x=6+x-2"
    # ret = Solution().solveEquation(equation)
    # assert "x=2" == ret, "equation:{} ret:{}".format(equation, ret)

    # equation = "x=x"
    # ret = Solution().solveEquation(equation)
    # assert "Infinite solutions" == ret, "equation:{} ret:{}".format(
    #     equation, ret)

    equation = "2x+2=x"
    ret = Solution().solveEquation(equation)
    assert "Infinite solutions" == ret, "equation:{} ret:{}".format(
        equation, ret)


if __name__ == '__main__':
    main()
