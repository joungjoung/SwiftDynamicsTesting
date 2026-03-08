"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:
    THAI_NUMBERS = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

    def max_num_power_1000(self, n: int) -> int:
        """
        หาจำนวนของเลขที่เป็นกำลังของ 1000 ที่น้อยที่สุดที่น้อยกว่าหรือเท่ากับ n
        """

        count = 0
        power_of_1000 = 1000
        while power_of_1000 <= n:
            count += 1
            power_of_1000 *= 1000
        return count
    
    def word_chunk_0(self, chunk: str) -> str:

        result = ""
        for i in range(len(chunk)):
            digit = int(chunk[i])
            if digit != 0:
                if i == 1 and digit == 2:
                    result += "ยี่"
                elif i == 1 and digit == 1:
                    result += ""
                elif i == 2 and digit == 1 and chunk[1] != "0":
                    result += "เอ็ด"
                else:
                    result += self.THAI_NUMBERS[digit]
                
                
                if i == 0:
                    result += "ร้อย"
                elif i == 1:
                    result += "สิบ"
        return result

    def word_chunk_odd(self, chunk: str) -> str:

        result = ""
        for i in range(len(chunk)):
            digit = int(chunk[i])
            if digit != 0:
                result += self.THAI_NUMBERS[digit]
                
                if i == 0:
                    result += "แสน"
                elif i == 1:
                    result += "หมื่น"
                elif i == 2:
                    result += "พัน"
        return result
    
    def word_chunk_even(self, chunk: str) -> str:
        return self.word_chunk_0(chunk) + "ล้าน"

    def number_to_thai(self, number: int) -> str:
        if number == 0:
            return "ศูนย์"

        num_colon = self.max_num_power_1000(number) + 1

        chunks = []
        str_num = str(number)
        for i in range(num_colon):
            # chunks.insert(0, str_num[-3:])
            chunks.append(str_num[-3:])
            str_num = str_num[:-3]
        chunks[len(chunks) - 1] = chunks[len(chunks) - 1].rjust(3, "0")

        result = ""
        for i in range(len(chunks) - 1, 0, -1):
            if i % 2 == 0:
                result += self.word_chunk_even(chunks[i])
            else:
                result += self.word_chunk_odd(chunks[i])
        result += self.word_chunk_0(chunks[0])
        return result


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    solution = Solution()
    print(solution.number_to_thai(number))
