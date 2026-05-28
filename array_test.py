import array

# numbers = array.array('i',[1,2,3,4,5])

# numbers = array.array('d',[1,2,3,4,5])

numbers = array.array('w',['a','b','c','d','e'])

# print(numbers[0])

# for i in numbers:
#     print(i, end=' ')

# print()
# print(numbers.typecode)

numbers.append('f')

reverse_arr = array.array(numbers.typecode, [])

for i in range(len(numbers)-1, -1, -1):
    print(i)
    reverse_arr.append(numbers[i])

print(reverse_arr)