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

for n in range(1, 31):
    print(f"number: {n}, factorial: {factorial_component(n)}, trailing zeroes: {count_trailing_zeroes(factorial(n))}")