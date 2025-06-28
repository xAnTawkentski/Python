#Exception Handling Exercises
#task1
try:
    numerator = float(input("Enter a number (numerator): "))
    denominator = float(input("Enter another number (denominator): "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

    #task2
try:
    user_input = input("Enter an integer: ")
    number = int(user_input)  # This will raise ValueError if input is not a valid integer
    print("You entered:", number)
except ValueError:
    print("Error: That is not a valid integer.")

#task3
filename = input("Enter the name of the file to open: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

#task4
def get_number(prompt):
    value = input(prompt)
    try:
        return float(value)
    except ValueError:
        raise TypeError(f"Invalid input '{value}'. A numeric value was expected.")

try:
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"The sum is: {num1 + num2}")
except TypeError as e:
    print("TypeError:", e)

#task5
filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except FileNotFoundError:
    print(f"Xato: '{filename}' nomli fayl topilmadi.")
except PermissionError:
    print(f"Xato: '{filename}' faylini ochishga sizda ruxsat yo‘q.")
except Exception as e:
    print(f"Kutilmagan xatolik yuz berdi: {e}")

#task6
royxat = [10, 20, 30, 40, 50]

try:
    indeks = int(input("Qaysi indeksdagi elementni ko‘rmoqchisiz? (0 dan boshlanadi): "))
    print(f"{indeks}-indeksdagi element: {royxat[indeks]}")
except IndexError:
    print("Xato: Siz kiritgan indeks ro'yxat chegarasidan tashqarida.")
except ValueError:
    print("Xato: Iltimos, butun son kiriting.")

#task7
try:
    raqam = input("Iltimos, biror raqam kiriting: ")
    print("Siz kiritdingiz:", raqam)
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi (KeyboardInterrupt). Dastur to‘xtadi.")

#task8
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    natija = a / b
    print(f"{a} ni {b} ga bo‘lish natijasi: {natija}")
except ArithmeticError:
    print("Xato: Arifmetik xato yuz berdi (masalan, nolga bo‘lish).")
except ValueError:
    print("Xato: Iltimos, raqam kiriting.")

#task9
filename = input("Ochmoqchi bo‘lgan fayl nomini kiriting: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl mazmuni:")
        print(content)
except UnicodeDecodeError:
    print(f"Xato: '{filename}' faylini o‘qishda kodlash (encoding) muammosi yuz berdi.")
except FileNotFoundError:
    print(f"Xato: '{filename}' fayli topilmadi.")
except PermissionError:
    print(f"Xato: '{filename}' faylini o‘qishga ruxsat yo‘q.")
except Exception as e:
    print(f"Kutilmagan xato yuz berdi: {e}")

#task10
my_list = [1, 2, 3]

try:
    # To'g'ri atributni chaqirish (masalan, append)
    my_list.append(4)
    print("Ro'yxatga element qo'shildi:", my_list)

    # Noto'g'ri atributni chaqirish (AttributeError yuzaga keladi)
    my_list.noto_attribut()
except AttributeError:
    print("Xato: Ro'yxatda bunday atribut mavjud emas (AttributeError).")

#File Input/Output Exercises - bu mavzu bizga darsda o'tilmagan, shu sabab mashqlar ishlanmadi, baholashda hisobga ol!

