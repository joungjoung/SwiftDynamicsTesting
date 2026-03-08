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



# AI Round1
def count_trailing_zeroes_AI1(n: int) -> int:
    """
    หาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial โดยการนับจำนวนเลขที่หารด้วย 5 ได้ลงตัว
    """

    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    return count

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

def components_5n_power_k(n: int, k: int) -> int:
    """
    หาจำนวนครั้งที่ 5^k เป็นตัวประกอบในเลข n! โดยการนับจำนวนเลขที่หารด้วย 5^k ได้ลงตัว
    """

    return n // (5 ** k)

def count_trailing_zeroes_my1(n: int) -> int:
    """
    หาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial
    โดย
     1. หาจำนวนที่เป็นเลขกำลังของ 5 ที่น้อยที่สุดที่น้อยกว่าหรือเท่ากับ n
     2. วน loop จาก 1 ถึงจำนวนที่เป็นเลขกำลังของ 5 ที่น้อยที่สุดที่น้อยกว่าหรือเท่ากับ n เพื่อหาจำนวนครั้งที่ 5^k เป็นตัวประกอบในเลข n! โดยการนับจำนวนเลขที่หารด้วย 5^k ได้ลงตัว
     3. นำผลลัพธ์ที่ได้จากข้อ 2 มารวมกันเพื่อหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial
    """

    loop_count = max_num_power_5(n)
    count = 0
    for k in range(1, loop_count + 1):
        count += components_5n_power_k(n, k)

    return count

for n in range(1, 126):
    # print(f"number: {n}, components of 5: {components_5n(n)}, components of 25: {components_25n(n)}, trailing zeroes: {count_trailing_zeroes(factorial(n))}")\
    # print(f"number: {n}, max power of 5: {max_num_power_5(n)}, trailing zeroes: {count_trailing_zeroes(factorial(n))}")
    
    # AI
    print(f"number: {n}, trailing zeros my1: {count_trailing_zeroes_my1(n)}, trailing zeroes v2: {count_trailing_zeroes_AI1(n)}")

