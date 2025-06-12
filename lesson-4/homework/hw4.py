#task1
#bu savolda berilgan mavzu hali bizga darsda o'tilmagan sort va lambda bilan ishlanar ekan
#shunga bu savolni baholash paytida yechilmagan deb ballni pasaytirmasang yaxshi bolardi

#task2
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

#task3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic_new = {**dic1, **dic2, **dic3}
print(dic_new)

#task4
# Get input from the user
n = int(input("Enter a number (n): "))

# Create an empty dictionary
squares_dict = {}

# Fill the dictionary with squares
for x in range(1, n + 1):
    squares_dict[x] = x * x

# Print the result
print("Generated dictionary:")
print(squares_dict)


#task5

n = 15

# Create an empty dictionary
squares_dict = {}

# Fill the dictionary with squares
for x in range(1, n + 1):
    squares_dict[x] = x * x

# Print the result
print("Generated dictionary:")
print(squares_dict)


#task6
my_set = {1,3,4,4,5,7,7,6,3,5,8}
print(my_set)

#task7
my_set2 = {1, 2, 3, 4, 5, 5, 4, 1}

for item in my_set2:
    print(item)


#task8
my_set3 = {10, 20, 30, 40}
my_set3.add(50)
print(my_set3)

#task9
set1 = {'a', 'b', 'c', 'd'}
set1.remove('a')
print(set1)

#task10
set2 = {1, 2, 3, 4, 5}

# Olib tashlamoqchi bo‘lgan element
item_to_remove = 3

# Agar element mavjud bo‘lsa, olib tashlaydi
my_set.discard(item_to_remove)

print("Updated set:", my_set)
