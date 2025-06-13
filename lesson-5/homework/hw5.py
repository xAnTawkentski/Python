#task1
year = int(input('please enter year:'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('This is leap year')
else:
    print('not leap year')



#task2
n = int(input("Enter integer number from 1 to 100: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

#task3
#solution with if-else statement:
a = int(input('enter number a :'))
b = int(input('enter number b :'))

if a % 2 == 0 and b % 2 == 0:
    print(list(range(a, b+1, 2)))
elif a % 2 == 0 and b % 2 != 0:
    print(list(range(a, b, 2)))
elif a % 2 != 0 and b % 2 != 0:
    print(list(range(a+1, b, 2 )))
elif a % 2 != 0 and b % 2 == 0:
    print(list(range(a+1, b+1, 2)))


#solution without if-else statement:
a = int(input('enter number a :'))
b = int(input('enter number b :'))
start = a + (a % 2)     # if 'a' is not even, the next even number
end = b - (b % 2)       # if 'b' is not even, the previous even number

print(list(range(start, end + 1, 2)))

