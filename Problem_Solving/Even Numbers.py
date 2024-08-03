n = int(input())
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
#     # _________________-
n = int(input())
print("\n".join(str(i) for i in range(1,n + 1) if i % 2 == 0))
    