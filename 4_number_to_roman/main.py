"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    ROMAN_NUMERALS_0 = ["0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    ROMAN_NUMERALS_1 = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ROMAN_NUMERALS_2 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    ROMAN_NUMERALS_3 = ["", "M", "MM", "MMM"]

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"

        if number > 3999:
            return "number can not greater than 3999"

        thousands = number // 1000
        hundreds = (number % 1000) // 100
        tens = (number % 100) // 10
        units = number % 10

        return self.ROMAN_NUMERALS_3[thousands] + self.ROMAN_NUMERALS_2[hundreds] + self.ROMAN_NUMERALS_1[tens] + self.ROMAN_NUMERALS_0[units]


if __name__ == "__main__":
    solution = Solution()

    print(solution.number_to_roman(0))    # 0
    print(solution.number_to_roman(1))    # I
    print(solution.number_to_roman(19))   # XIX
    print(solution.number_to_roman(999))  # CMXCIX
    print(solution.number_to_roman(101))  # CI
    print(solution.number_to_roman(-1))   # number can not less than 0
    print(solution.number_to_roman(4000)) # number can not greater than 3999
