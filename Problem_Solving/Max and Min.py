A, B, C = map(int, input().split())
if A > B and A > C:
    max_val = A
    if B > C:
        min_val = C
    else:
        min_val = B
elif B > A and B > C:
    max_val = B
    if A > C:
        min_val = C
    else:
        min_val = A
else:
    max_val = C
    if A > B:
        min_val = B
    else:
        min_val = A
print(min_val,max_val)
