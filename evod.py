import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

nums = list(map(int, input("Enter numbers: ").split()))
evens = sum(1 for x in nums if x % 2 == 0)
odds = len(nums) - evens

print(f"Even: {evens}, Odd: {odds}")
for num in nums:
    print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}")
