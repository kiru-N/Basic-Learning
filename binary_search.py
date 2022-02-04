# Binary search
# ----------------


li = [1, 10, 20, 30, 40, 50, 60]

x = 30

start = 0
end = len(li) - 1

print(start, end)

while end >= start:
    mid = start + (end - start) // 2

    if li[mid] == x:
        print('Position of %d is' % x, mid)
        break
    elif x > li[mid]:
        start = mid +1
    else:
        end = mid -1

else:
    print('%d is not found'%x)

