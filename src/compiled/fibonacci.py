prev1 = 0
prev2 = 1
cur = 1
i = 0
test = ((0 + 1) - 2)
print(prev1)
print(prev2)
while (i < 50):
    cur = (prev1 + prev2)
    prev1 = prev2
    prev2 = cur
    i = (i + 1)
    print(cur)