#OOP
#task1
import math

# Doira klassi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Doira yuzasini hisoblash
    def area(self):
        return math.pi * self.radius ** 2

    # Doira perimetrini hisoblash
    def perimeter(self):
        return 2 * math.pi * self.radius

# Foydalanish (sinov uchun)
r = float(input("Doira radiusini kiriting: "))

doira = Circle(r)

print(f"Doira yuzasi: {doira.area():.2f}")
print(f"Doira perimetri: {doira.perimeter():.2f}")

#task2
from datetime import date

class Person:
    def __init__(self,name,country,birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate
    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthdate.year

# Agar tug‘ilgan kun hozirgi sanadan keyin bo‘lsa, yoshni 1 ga kamaytiramiz
        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

# Misol foydalanish:
person = Person("Ali", "O'zbekiston", date(1990, 5, 15))
print(person.calculate_age())
    
#task3
class Calculator:
    def __init__(self):
        pass

    def qoshish(self, a, b):
        return a + b

    def ayirish(self, a, b):
        return a - b

    def kopaytirish(self, a, b):
        return a * b

    def bolish(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Nolga bo‘lish mumkin emas"

# Foydalanuvchidan sonlarni olish
a = float(input('a sonni kiriting: '))
b = float(input('b sonni kiriting: '))

# Kalkulyator obyektini yaratish
calc = Calculator()

# Natijalarni chiqarish
print(f"Yig‘indi: {calc.qoshish(a, b)}")
print(f"Ayirma: {calc.ayirish(a, b)}")
print(f"Ko‘paytma: {calc.kopaytirish(a, b)}")
print(f"Bo‘linma: {calc.bolish(a, b)}")


    #task4
import math

# Asosiy shakl klassi
class Shape:
    def area(self):
        raise NotImplementedError("Yuza hisoblash metodi aniqlanmagan")

    def perimeter(self):
        raise NotImplementedError("Perimetr hisoblash metodi aniqlanmagan")

# Doira klassi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Kvadrat klassi
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Uchburchak klassi (uch tomonli)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Geron formulasi
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# ==== SINOV QISMI ====

# Doira sinovi
radius = float(input("Doira radiusini kiriting: "))
circle = Circle(radius)
print(f"Doira yuzi: {circle.area():.2f}")
print(f"Doira perimetri: {circle.perimeter():.2f}")

# Kvadrat sinovi
side = float(input("\nKvadrat tomoni uzunligini kiriting: "))
square = Square(side)
print(f"Kvadrat yuzi: {square.area():.2f}")
print(f"Kvadrat perimetri: {square.perimeter():.2f}")

# Uchburchak sinovi
a = float(input("\nUchburchakning 1-tomonini kiriting: "))
b = float(input("Uchburchakning 2-tomonini kiriting: "))
c = float(input("Uchburchakning 3-tomonini kiriting: "))
triangle = Triangle(a, b, c)
print(f"Uchburchak yuzi: {triangle.area():.2f}")
print(f"Uchburchak perimetri: {triangle.perimeter():.2f}")


#task5
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)
        else:
            pass  # teng qiymatlar qo‘shilmaydi

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

# ======== FOYDALANISH (interaktiv sinov) ========

bst = BinarySearchTree()

# BST ga elementlar qo‘shish
n = int(input("Nechta son kiritmoqchisiz? "))
for _ in range(n):
    son = int(input("Sonni kiriting: "))
    bst.insert(son)

# Qidiruv
qidir = int(input("\nQidirilayotgan sonni kiriting: "))
if bst.search(qidir):
    print(f"{qidir} daraxtda mavjud ✅")
else:
    print(f"{qidir} daraxtda topilmadi ❌")


#task6
class Stack:
    def __init__(self):
        self.items = []  # bo‘sh ro‘yxat — stack uchun

    def push(self, item):
        self.items.append(item)  # element qo‘shish

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # oxirgi elementni chiqarish
        else:
            return "Stack bo‘sh, pop qilish mumkin emas."

    def is_empty(self):
        return len(self.items) == 0  # stack bo‘shmi?

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # oxirgi elementni ko‘rsatish
        else:
            return None

    def size(self):
        return len(self.items)  # stackdagi elementlar soni

# ======= SINOV QISMI =======

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stackdagi oxirgi element:", stack.peek())  # 30
print("Stackdan chiqarilgan element:", stack.pop())  # 30
print("Yangi oxirgi element:", stack.peek())  # 20
print("Stack bo‘shmi?", stack.is_empty())  # False
print("Stackdagi elementlar soni:", stack.size())  # 2


#task7
class Node:
    def __init__(self, data):
        self.data = data      # Tugundagi ma'lumot
        self.next = None      # Keyingi tugunga havola

class LinkedList:
    def __init__(self):
        self.head = None      # Ro'yxat boshini saqlaydi

    def display(self):
        current = self.head
        if current is None:
            print("Ro'yxat bo‘sh.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    def insert(self, data, position=None):
        new_node = Node(data)
        if position is None or position == 0:
            # Boshlanishga qo‘shish
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            current_pos = 0
            while current and current_pos < position:
                prev = current
                current = current.next
                current_pos += 1
            if prev is None:
                # Agar ro'yxat bo‘sh bo‘lsa boshiga qo‘shish
                self.head = new_node
            else:
                prev.next = new_node
            new_node.next = current

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:
                    # Boshlang‘ich tugunni o‘chirish
                    self.head = current.next
                else:
                    prev.next = current.next
                print(f"{data} qiymatli tugun o‘chirildi.")
                return
            prev = current
            current = current.next
        print(f"{data} qiymatli tugun topilmadi.")

# ====== Foydalanish misoli ======

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # Chiqarish: 30 -> 20 -> 10

ll.insert(25, 2) 
ll.display()  # Chiqarish: 30 -> 20 -> 25 -> 10

ll.delete(20)
ll.display()  # Chiqarish: 30 -> 25 -> 10

ll.delete(100)  # Tugun topilmadi haqida xabar


#task8
class ShoppingCart:
    def __init__(self):
        self.items = {}  # Mahsulot nomi: narxi

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"'{item_name}' savatchaga qo‘shildi, narxi: {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"'{item_name}' savatchadan o‘chirildi.")
        else:
            print(f"'{item_name}' savatchada yo‘q.")

    def total_price(self):
        return sum(self.items.values())

    def show_cart(self):
        if not self.items:
            print("Savatcha bo‘sh.")
        else:
            print("Savatchadagi mahsulotlar:")
            for item, price in self.items.items():
                print(f"- {item}: {price}")
            print(f"Jami narx: {self.total_price()}")

# ====== Foydalanish misoli ======

cart = ShoppingCart()

cart.add_item("Olma", 3000)
cart.add_item("Banan", 2500)
cart.show_cart()

cart.remove_item("Olma")
cart.show_cart()

print("Umumiy narx:", cart.total_price())


#task9
class Stack:
    def __init__(self):
        self.items = []  # Bo‘sh ro‘yxat — stack uchun

    def push(self, item):
        self.items.append(item)  # Element qo‘shish

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Oxirgi elementni chiqarish
        else:
            return "Stack bo‘sh, pop qilish mumkin emas."

    def is_empty(self):
        return len(self.items) == 0  # Stack bo‘shligini tekshirish

    def display(self):
        if self.is_empty():
            print("Stack bo‘sh.")
        else:
            print("Stackdagi elementlar:")
            for item in reversed(self.items):
                print(item)

# ======= SINOV QISMI =======

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()  # 30, 20, 10

print("Pop qilingan element:", stack.pop())  # 30

stack.display()  # 20, 10


#task10
class Queue:
    def __init__(self):
        self.items = []  # Bo‘sh ro‘yxat — queue uchun

    def enqueue(self, item):
        self.items.append(item)  # Elementni navbat oxiriga qo‘shish

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Navbat boshidan element chiqarish
        else:
            return "Queue bo‘sh, dequeue qilish mumkin emas."

    def is_empty(self):
        return len(self.items) == 0  # Queue bo‘shligini tekshirish

    def display(self):
        if self.is_empty():
            print("Queue bo‘sh.")
        else:
            print("Queuedagi elementlar:")
            for item in self.items:
                print(item)

# ======= SINOV QISMI =======

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()  # 10, 20, 30

print("Dequeue qilingan element:", queue.dequeue())  # 10

queue.display()  # 20, 30


#task11
class Bank:
    def __init__(self):
        self.customers = {}  # mijozlar: {ismi: balans}

    def create_account(self, name, initial_deposit=0):
        if name in self.customers:
            print(f"{name} nomli hisob allaqachon mavjud.")
        else:
            self.customers[name] = initial_deposit
            print(f"{name} nomli yangi hisob yaratildi. Balans: {initial_deposit}")

    def deposit(self, name, amount):
        if name in self.customers:
            if amount > 0:
                self.customers[name] += amount
                print(f"{name} hisobiga {amount} qo‘shildi. Yangi balans: {self.customers[name]}")
            else:
                print("Qo‘shiladigan summa musbat bo‘lishi kerak.")
        else:
            print(f"{name} nomli hisob topilmadi.")

    def withdraw(self, name, amount):
        if name in self.customers:
            if 0 < amount <= self.customers[name]:
                self.customers[name] -= amount
                print(f"{name} hisobidan {amount} yechildi. Yangi balans: {self.customers[name]}")
            else:
                print("Mablag‘ yetarli emas yoki noto‘g‘ri summa kiritildi.")
        else:
            print(f"{name} nomli hisob topilmadi.")

    def check_balance(self, name):
        if name in self.customers:
            print(f"{name} hisobidagi balans: {self.customers[name]}")
        else:
            print(f"{name} nomli hisob topilmadi.")

# ====== Foydalanish misoli ======

bank = Bank()

bank.create_account("Ali", 1000)
bank.create_account("Vali")

bank.deposit("Ali", 500)
bank.withdraw("Vali", 100)  # Hisob yo‘q, shuning uchun xato

bank.deposit("Vali", 200)
bank.withdraw("Ali", 300)

bank.check_balance("Ali")
bank.check_balance("Vali")


