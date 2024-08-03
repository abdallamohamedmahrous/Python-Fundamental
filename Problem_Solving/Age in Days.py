N = int(input())
print(f"{N // 365} years")
N %= 365
print(f"{N // 30} months")
N %= 30
print(f"{N} days")
