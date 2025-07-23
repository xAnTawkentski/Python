#task1
from datetime import datetime

def age_calculator():
    # Foydalanuvchidan tug‘ilgan sanani so‘rash
    birth_date_str = input("Tug‘ilgan sanangizni kiriting (yyyy-mm-dd formatda): ")
    
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()

        # Tug‘ilgan sanadan bugungi kungacha bo‘lgan farq
        delta = today - birth_date

        # To‘liq yillar, oylar va kunlarni hisoblash
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            last_month = (today.month - 1) or 12
            last_month_year = today.year if today.month != 1 else today.year - 1
            days_in_last_month = (datetime(last_month_year, last_month + 1, 1) - datetime(last_month_year, last_month, 1)).days
            days += days_in_last_month

        if months < 0:
            years -= 1
            months += 12

        # Natijani chiqarish
        print(f"Siz {years} yil, {months} oy, {days} kunliksiz.")

    except ValueError:
        print("Iltimos, sanani to‘g‘ri formatda kiriting! (Masalan: 2000-05-12)")

# Dastur ishga tushiriladi
age_calculator()


#task2
from datetime import datetime, timedelta

def days_until_next_birthday():
    # Foydalanuvchidan tug‘ilgan sanani olish
    birth_date_str = input("Tug‘ilgan sanangizni kiriting (yyyy-mm-dd formatda): ")
    
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()

        # Keyingi tug‘ilgan kunni aniqlash
        this_year_birthday = birth_date.replace(year=today.year)

        if this_year_birthday < today:
            next_birthday = birth_date.replace(year=today.year + 1)
        else:
            next_birthday = this_year_birthday

        days_left = (next_birthday - today).days

        print(f"Sizning keyingi tug‘ilgan kuningizgacha {days_left} kun qoldi.")

    except ValueError:
        print("Iltimos, sanani to‘g‘ri formatda kiriting! (Masalan: 2000-05-12)")

# Dastur ishga tushiriladi
days_until_next_birthday()


#task3
from datetime import datetime, timedelta

def meeting_scheduler():
    try:
        # Foydalanuvchidan hozirgi sana va vaqtni olish
        current_datetime_str = input("Hozirgi sana va vaqtni kiriting (yyyy-mm-dd HH:MM formatda): ")
        current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")

        # Uchrashuv davomiyligini soat va daqiqalarda olish
        hours = int(input("Uchrashuv davomiyligi (soat): "))
        minutes = int(input("Uchrashuv davomiyligi (daqiqa): "))

        # Davomiylikni qo‘shish
        meeting_duration = timedelta(hours=hours, minutes=minutes)
        end_datetime = current_datetime + meeting_duration

        # Natijani chiqarish
        print(f"Uchrashuv {end_datetime.strftime('%Y-%m-%d %H:%M')} da tugaydi.")

    except ValueError:
        print("Iltimos, barcha qiymatlarni to‘g‘ri formatda kiriting!")

# Dastur ishga tushuriladi
meeting_scheduler()


#task4
from datetime import datetime
import pytz

def timezone_converter():
    try:
        # Sana va vaqtni kiritish
        date_str = input("Sana va vaqtni kiriting (yyyy-mm-dd HH:MM formatda): ")
        input_timezone_str = input("Hozirgi timezone nomini kiriting (masalan: Asia/Tashkent): ")
        target_timezone_str = input("O‘zgartirmoqchi bo‘lgan timezone (masalan: US/Eastern): ")

        # Vaqt obyektini yaratish
        naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

        # Vaqt zonalarini olish
        input_timezone = pytz.timezone(input_timezone_str)
        target_timezone = pytz.timezone(target_timezone_str)

        # Vaqtni lokalizatsiya qilish
        local_datetime = input_timezone.localize(naive_datetime)

        # Vaqtni boshqa timezonega konvertatsiya qilish
        target_datetime = local_datetime.astimezone(target_timezone)

        # Natijani chiqarish
        print(f"\n{input_timezone_str} vaqti: {local_datetime.strftime('%Y-%m-%d %H:%M')}")
        print(f"{target_timezone_str} vaqti: {target_datetime.strftime('%Y-%m-%d %H:%M')}")

    except Exception as e:
        print("Xatolik yuz berdi:", e)
        print("Ehtimol, timezone nomi noto‘g‘ri yoki format xato. Iltimos, qayta tekshirib ko‘ring.")

# Dastur ishga tushuriladi
timezone_converter()



#task5
from datetime import datetime
import time

def countdown_timer():
    # Foydalanuvchidan kelajakdagi sana-vaqtni olish
    future_str = input("Kelajakdagi sana va vaqtni kiriting (yyyy-mm-dd HH:MM:SS formatda): ")

    try:
        future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

        while True:
            now = datetime.now()
            remaining = future_time - now

            if remaining.total_seconds() <= 0:
                print("\n⏰ Vaqt tugadi!")
                break

            # Qolgan vaqtni formatlash
            days = remaining.days
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Ekranni yangilash (shu qatorda yozish uchun \r)
            print(f"\r⏳ Qolgan vaqt: {days} kun, {hours:02} soat, {minutes:02} daqiqa, {seconds:02} soniya", end="")

            time.sleep(1)  # Har 1 soniyada yangilab turish

    except ValueError:
        print("⚠️ Iltimos, sanani to‘g‘ri formatda kiriting! Masalan: 2025-08-01 18:00:00")

# Dastur ishga tushuriladi
countdown_timer()


#task6
import re

def validate_email():
    email = input("Email manzilingizni kiriting: ")

    # Oddiy, umumiy email format uchun regex
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        print("✅ Email manzili to‘g‘ri formatda.")
    else:
        print("❌ Email manzili noto‘g‘ri formatda. Iltimos, qayta tekshirib ko‘ring.")

# Dastur ishga tushuriladi
validate_email()


#task7
def format_phone_number():
    phone = input("Telefon raqamingizni kiriting (faqat raqamlar): ")

    # Faqat raqamlar kirganini tekshirish
    if not phone.isdigit():
        print("❌ Iltimos, faqat raqamlardan foydalaning.")
        return

    # Raqamlar sonini tekshirish (10ta raqam bo'lishi kerak)
    if len(phone) != 10:
        print("❌ Telefon raqami aniq 10 ta raqamdan iborat bo'lishi kerak.")
        return

    # Formatlash: (123) 456-7890
    area_code = phone[:3]
    middle = phone[3:6]
    last = phone[6:]
    formatted = f"({area_code}) {middle}-{last}"

    print("✅ Formatlangan raqam:", formatted)

# Dastur ishga tushuriladi
format_phone_number()


#task8
import re

def check_password_strength():
    password = input("Parolni kiriting: ")

    # Shartlar ro‘yxati
    length_ok = len(password) >= 8
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)

    # Baholash
    if length_ok and has_upper and has_lower and has_digit:
        print("✅ Parol kuchli!")
    else:
        print("❌ Parol kuchsiz. Quyidagi shartlarga e'tibor bering:")
        if not length_ok:
            print("- Kamida 8 ta belgidan iborat bo‘lishi kerak.")
        if not has_upper:
            print("- Kamida 1 ta katta harf kerak (A-Z).")
        if not has_lower:
            print("- Kamida 1 ta kichik harf kerak (a-z).")
        if not has_digit:
            print("- Kamida 1 ta raqam kerak (0-9).")

# Dastur ishga tushuriladi
check_password_strength()



#task9
def word_finder():
    # Misol matn
    sample_text = """
    Python is a powerful programming language. Many developers use Python for web development,
    data analysis, AI, automation, and more. Python's syntax is clean and easy to learn.
    """

    # Foydalanuvchidan so‘z kiritish
    word = input("Qaysi so‘zni qidirmoqchisiz? ").strip()

    # Matn va so‘zni kichik harfga o'tkazish (case-insensitive qidiruv uchun)
    text_lower = sample_text.lower()
    word_lower = word.lower()

    index = 0
    occurrences = []

    # Qidirish
    while index < len(text_lower):
        index = text_lower.find(word_lower, index)
        if index == -1:
            break
        occurrences.append(index)
        index += len(word_lower)

    # Natijani chiqarish
    if occurrences:
        print(f"\n🔍 So‘z '{word}' {len(occurrences)} marta topildi. Joylashuvi (indekslar):")
        for i, pos in enumerate(occurrences, 1):
            print(f"{i}) Belgidan boshlab: {pos}")
    else:
        print(f"❌ So‘z '{word}' matndan topilmadi.")

# Dastur ishga tushuriladi
word_finder()


#task10
import re

def extract_dates():
    text = input("Matn kiriting (sanalari bilan): ")

    # Regex patternlar ro'yxati
    date_patterns = [
        r"\b\d{2}/\d{2}/\d{4}\b",            # 23/07/2025
        r"\b\d{2}-\d{2}-\d{4}\b",            # 23-07-2025
        r"\b\d{4}-\d{2}-\d{2}\b",            # 2025-07-23
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b",  # July 23, 2025
    ]

    found_dates = []

    for pattern in date_patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        found_dates.extend(matches)

    if found_dates:
        print("\n📅 Topilgan sanalar:")
        for i, date in enumerate(found_dates, 1):
            print(f"{i}) {date}")
    else:
        print("❌ Hech qanday sana topilmadi.")

# Dastur ishga tushuriladi
extract_dates()



