nums = [0,1,2,3,4,5,6,7]
for num in nums:
    if num == 4:
        print('found!')
        break
    print(num)

nums = [0,1,2,3,4,5,6,7]
for num in nums:
    if num == 4:
        print('i found!')
        continue
    print(num)