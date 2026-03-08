def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n ต้องเป็นจำนวนเต็มไม่ติดลบ")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_component(n: int) -> list[int]:
    result = []
    for i in range(1, n + 1):
        result.append(i)
    return result

def count_trailing_zeroes(n: int) -> int:
    if n < 0:
        raise ValueError("n ต้องเป็นจำนวนเต็มไม่ติดลบ")
    
    count = 0
    while n % 10 == 0 and n != 0:
        count += 1
        n //= 10
    return count

def components_5n(n: int) -> int:
    """
    หาจำนวนครั้งที่ 5 เป็นตัวประกอบในเลข n! โดยการนับจำนวนเลขที่หารด้วย 5 ได้ลงตัว
    """

    return n // 5

def components_25n(n: int) -> int:
    """
    หาจำนวนครั้งที่ 25 เป็นตัวประกอบในเลข n! โดยการนับจำนวนเลขที่หารด้วย 25 ได้ลงตัว
    """

    return n // 25

def max_num_power_5(n: int) -> int:
    """
    หาจำนวนของเลขที่เป็นกำลังของ 5 ที่น้อยที่สุดที่น้อยกว่าหรือเท่ากับ n
    """

    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += 1
        power_of_5 *= 5
    return count


for n in range(1, 126):
    # print(f"number: {n}, components of 5: {components_5n(n)}, components of 25: {components_25n(n)}, trailing zeroes: {count_trailing_zeroes(factorial(n))}")\
    print(f"number: {n}, max power of 5: {max_num_power_5(n)}, trailing zeroes: {count_trailing_zeroes(factorial(n))}")