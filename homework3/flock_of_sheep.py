flock_sheep = [5,7,300,90,24,50,75]
print('Hello, my name is Dat and these are my sheep sizes')
print(flock_sheep)
print()
for i in range(3):
    print(f'month {i+1}')
    length = len(flock_sheep)
    for j in range(length):
        flock_sheep[j]=flock_sheep[j] + 50
    print('One month has passed, now here is my flock')
    print(flock_sheep)

    if 3 - i == 1:
        print()
        break
    else: 
        max = flock_sheep[0]
        for k in flock_sheep[1:]:
            if max < k:
                max = k
        print(f'Now my biggest sheep has size {max} let\' shear it')

        change = flock_sheep.index(max)
        flock_sheep[change] = 8
        print('After shearing, here is my flock')
        print(flock_sheep)
        print()

sum=0
for i in range(length):
    sum=sum + flock_sheep[i]
print(f'My flock has size in total: {sum}')
print(f'I would get {sum} * 2$ = {sum*2}$')
# #tìm max
# max = flock_sheep[0]
# for i in flock_sheep[1:]:
#     if max < i:
#         max = i
# print(f'Now my biggest sheep has size {max} let\' shear it')

# #chuyển max ->8
# change = flock_sheep.index(max)
# flock_sheep[change] = 8
# print('After shearing, here is my flock')
# print(flock_sheep)

# # cừu lớn
# length = len(flock_sheep)
# for i in range(length):
#     flock_sheep[i]=flock_sheep[i] + 50
# print('One month has passed, now here is my flock')
# print(flock_sheep)
