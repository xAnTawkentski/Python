#task1
name=input("Input your name :")
birth = int(input("Input your birth year :"))
age = 2025 - birth

print(f"{name}'s age = {age}")

#task2
txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]

print(f"Car names : {car1}, {car2}")

#task3
txt = 'MsaatmiazD'
car1 = txt[::2]
car2 = txt[::-2]
print(f"Car names : {car1}, {car2}")

#task4
txt = "I'am John. I am from London"
residence = txt[-6:]
print(f"residence : {residence}")

#task5
text = input("Please enter text :")
reversed_text = text[::-1]

print(f"Reversed text : {reversed_text}")


#task6
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#task7
# Foydalanuvchidan sonlarni kiritish
sonlar_str = input("Sonlarni kiriting (probel bilan): ")

# Matnni bo'lib, sonlar ro'yxatiga aylantirish (float yoki int)
sonlar = list(map(float, sonlar_str.split()))
sonlar

# Eng katta sonni topish
eng_katta = max(sonlar)

# Natijani chiqarish
print("Eng katta son:", eng_katta)


#task8
# Foydalanuvchidan so'z olish
soz = input("So'z kiriting: ")

# So'zni teskari qilib ko'rish
teskari = soz[::-1]

# Solishtirish
if soz == teskari:
    print("Bu so'z palindrom.")
else:
    print("Bu so'z palindrom emas.")

#task9
# Foydalanuvchidan email manzilini olish
email = input("Email manzilini kiriting: ")

# '@' belgisi bo'yicha bo'lib, domen qismini ajratish
qismlar = email.split('@')

# Domen qismi 2-element bo'ladi (indeksi 1)
if len(qismlar) == 2:
    domen = qismlar[1]
    print("Domen qismi:", domen)
else:
    print("Xato: To'g'ri email manzili kiriting!")


#task10
import random
import string

# Parol uzunligini belgilash
uzunlik = int(input("Parol uzunligini kiriting: "))

# Belgilar to'plami: harflar, raqamlar, maxsus belgilar
harflar = string.ascii_letters       # a-z + A-Z
raqamlar = string.digits             # 0-9
belgilar = string.punctuation        # !@#$%^&*()_+...

# Hammasini birlashtiramiz
barcha_belgilar = harflar + raqamlar + belgilar

# Tasodifiy parol yaratamiz
parol = ''.join(random.choice(barcha_belgilar) for _ in range(uzunlik))

# Natijani chiqaramiz
print("Yaratilgan parol:", parol)


