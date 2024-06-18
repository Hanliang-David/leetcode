class Solution:
    def reverse(self, x: int) -> int:
        sign = 0
        if x > 0:
            sign = 1
        elif x < 0:
            sign = -1

        abs_x = abs(x)
        str_x = str(abs_x)
        reversed_str = str_x[::-1]
        result = sign * int(reversed_str)

        if result > (pow(2, 31) - 1) or result < -pow(2, 31):
            return 0
        else:
            return result
