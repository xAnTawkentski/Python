#task1
txt = input("Matnni kiriting: ")
vowels = 'aeiouAEIOU'
natija = ''
count = 0
i = 0

while i < len(txt):
    natija += txt[i]
    count += 1

    if count == 3:
        if i < len(txt) - 1 and (txt[i] in vowels or txt[i + 1] == '_'):
            # Undan keyingi belgi mavjud va shartlar bajarilsa
            i += 1
            natija += txt[i]
            if i < len(txt) - 1:
                natija += '_'
        else:
            if i < len(txt) - 1:
                natija += '_'
        count = 0
    i += 1

print(natija)

#task2
n = int(input('0 dan 20gacha biror butun son kiriting:'))

if 0 <= n < 20:
    i = 0
    while 0 <= i < n:
        print(i**2)
        i += 1
elif n < 0 or n >= 20:
    print('n qiymati xato')

#task3
#Exercise 1:
i = 1
while i <= 10:
    print(i)
    i+=1

#Exercise 2:
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end= ' ')
    print()

#Exercise 3:
n = int(input('Enter integer number: '))

sum = 0  # yig'indi uchun o'zgaruvchi

for i in range(1, n+1):
    sum += i  # har bir i ni yig'indiga qo'shish

print("Sum is:", sum)

#Exercise 4:
n = int(input('Enter integer number: '))

for i in range(1, 11):
    print(n * i)

#Exercise 5:
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break  # 500 dan katta bo‘lsa — siklni to‘xtatadi
    if num > 150:
        continue  # 150 dan katta bo‘lsa — bu sonni o‘tkazib yuboradi
    if num % 5 == 0:
        print(num)


#Exercise 6:
num = int(input("Enter a number: "))

count = 0
while num != 0:
    num = num // 10  # sonni 10 ga bo‘lib qisqartiramiz
    count += 1       # har safar bitta raqam yo‘qoladi → hisob 1 ga oshadi

print("Total digits:", count)


#Exercise 7:
for i in range(5, 0, -1):         # i = 5, 4, 3, 2, 1
    for j in range(i, 0, -1):     # j = i dan 1 gacha teskari
        print(j, end=' ')
    print()  # har qatordan keyin yangi qatorga o‘tish


#Exercise 8:
list1 = [10, 20, 30, 40, 50]

for i in list[10,20,30,40,50]:
    print(i)

#Exercise 9:
#solution1:
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
    

#solution2:
list1 = [10, 20, 30, 40, 50]

for num in reversed(list1):
    print(num)


#Exercise 10:
for i in range(5):
    print(i)
print("Done!")


#Exercise 11:
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)


#Exercise 12:
n_terms = 10
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n_terms):
    print(a, end="  ")
    a, b = b, a + b

#Exercise 13:
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")


#task 4
def uncommon_elements(list1, list2):
    result = []

    temp_list2 = list2.copy()
    for item in list1:
        if item in temp_list2:
            temp_list2.remove(item)  # bir marta uchrashganini o‘chir
        else:
            result.append(item)

    temp_list1 = list1.copy()
    for item in list2:
        if item in temp_list1:
            temp_list1.remove(item)
        else:
            result.append(item)

    return result

# Misollar
print(uncommon_elements([1, 1, 2], [2, 3, 4]))       # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))       # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]



