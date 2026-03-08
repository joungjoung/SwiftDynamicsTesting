"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not blank"
        
        max_index = 0
        for i in range(1, len(numbers)):
            if numbers[i] > numbers[max_index]:
                max_index = i
        return max_index

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [1, 2, 1, 3, 5, 6, 4],
        [],
        [5, 5, 5, 5],
        [10],
        [-1, -2, -3, -4]
    ]
    for numbers in test_cases:
        result = solution.find_max_index(numbers)
        print(f"numbers: {numbers}, index of max: {result}")
