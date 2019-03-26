def countBitSet(n):
    count = 0
    while(n):
        n =n&(n-1)
        count += 1
    return count


for i in [2**i for i in range(10)]:
    # print(i)
    print(countBitSet(i))
print("---------------------")
for i in [3**i for i in range(10)]:
    # print(i)
    print(countBitSet(i))
    