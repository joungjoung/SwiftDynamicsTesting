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
    
    def max_num_power_5(self, n: int) -> int:
        """
        หาจำนวนของเลขที่เป็นกำลังของ 5 ที่น้อยที่สุดที่น้อยกว่าหรือเท่ากับ n
        """

        count = 0
        power_of_5 = 5
        while power_of_5 <= n:
            count += 1
            power_of_5 *= 5
        return count
    
    def components_5n_power_k(self, n: int, k: int) -> int:
        """
        หาจำนวนครั้งที่ 5^k เป็นตัวประกอบในเลข n! โดยการนับจำนวนเลขที่หารด้วย 5^k ได้ลงตัว
        """

        return n // (5 ** k)
    
    def find_tailing_zeroes(self, number: int) -> int | str:
        """
        หาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial
        โดย
         1. หาจำนวนที่เป็นเลขกำลังของ 5 ที่น้อยที่สุดที่น้อยกว่าหรือเท่ากับ number
         2. วน loop จาก 1 ถึงจำนวนที่เป็นเลขกำลังของ 5 ที่น้อยที่สุดที่น้อยกว่าหรือเท่ากับ number เพื่อหาจำนวนครั้งที่ 5^k เป็นตัวประกอบในเลข number! โดยการนับจำนวนเลขที่หารด้วย 5^k ได้ลงตัว
         3. นำผลลัพธ์ที่ได้จากข้อ 2 มารวมกันเพื่อหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial
        """
    
        loop_count = self.max_num_power_5(number)
        count = 0
        for k in range(1, loop_count + 1):
            count += self.components_5n_power_k(number, k)
    
        return count


if __name__ == "__main__":
    solution = Solution()
    for n in range(1, 31):
        result = solution.find_tailing_zeroes(n)
        print(f"number: {n}, tailing zeroes: {result}")
