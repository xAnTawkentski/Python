#task1
fruits = ['apple', 'banana', 'cherry', 'watermelon', 'melon']
print(fruits[2])

#task2
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)

#task3
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers [-1]
result = [first, middle, last]
print(result)

#task4
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)

#task5
cities = ['London', 'Tashkent', 'Paris', 'Mexico']
if 'Paris' in cities:
    print('Paris is in the list')
else: print('Paris is not in the list')

#task6
numbers = [1,2,3,4,5]
dublicated = numbers * 2
print(dublicated)

#task7
numbers = [1,2,3,4,5,6,7]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

#task8
numbers = (1,2,3,4,5,6,7,8,9,10)
sliced = numbers[3:8]
print(sliced)

#task 9
colors = ('red', 'green', 'blue', 'black', 'white', 'blue', 'blue')

count_blue = 0

for color in colors:
    if color == 'blue':
        count_blue += 1
print(count_blue)

#task10
animals = ('bear', 'lion', 'tiger')

if 'lion' in animals:
    index_lion = animals.index('lion')
    print('Index of "lion" :',index_lion)
else:
    print(' "lion" is not in the tuple')

#task11
tuple1 = (1,2,3)
tuple2 = (4,5,6)
merged_tuple = tuple1 + tuple2

print("merged tuple : ",merged_tuple)

#task12
list1 = [1,2,3,4]
tuple1 = (3,5,6,7,8)
len_list1 = len(list1)
len_tuple1 = len(tuple1)
print("lenght list:",len_list1)
print("lenght tuple:",len_tuple1)

#task13
num_tuple = (1,2,3,4,5)
num_list = list(num_tuple)
print(num_list)

#task14
tuple_numbers = (1,3,6,3,8,9)
max_tuple = max(tuple_numbers)
min_tuple = min(tuple_numbers)
print("max =",max_tuple)
print("min =",min_tuple)

#task15
words = ('apple', 'banana', 'cherry')
reversed_words = words[::-1]

print("reversed tuple :",reversed_words)
