"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    
    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("n ต้องเป็นจำนวนเต็มไม่ติดลบ")
    
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        
        factorial_value = self.factorial(number)
        count = 0
        while factorial_value % 10 == 0 and factorial_value != 0:
            count += 1
            factorial_value //= 10
        return count


if __name__ == "__main__":
    solution = Solution()
    for n in range(1, 31):
        result = solution.find_tailing_zeroes(n)
        print(f"number: {n}, tailing zeroes: {result}")
