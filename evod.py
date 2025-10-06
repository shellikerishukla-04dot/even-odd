nums = list(map(int, input("Enter numbers: ").split()))
evens = sum(1 for x in nums if x % 2 == 0)
odds = len(nums) - evens
print("Even:", evens, "Odd:", odds)
