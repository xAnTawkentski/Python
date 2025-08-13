#task1
import sqlite3

# Ma'lumotlar bazasiga ulanish (yangi bazani yaratadi agar mavjud bo'lmasa)
conn = sqlite3.connect('example.db')

# Cursor obyekti yaratish (SQL so'rovlarini bajarish uchun)
cursor = conn.cursor()

# Roster jadvalini yaratish (Name va Species - text, Age - integer)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# O'zgarishlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

print("Database and Roster table created successfully.")


#task2
import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Jadvalga ma'lumotlar qo'shish
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', data)

# O'zgarishlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

print("Data inserted successfully into Roster table.")


#task3
import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Name ni yangilash
cursor.execute('''
    UPDATE Roster
    SET Name = ?
    WHERE Name = ?
''', ("Ezri Dax", "Jadzia Dax"))

# O'zgarishlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

print("Name updated successfully.")


#task4
import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Bajoranlarni tanlash
cursor.execute('''
    SELECT Name, Age
    FROM Roster
    WHERE Species = ?
''', ("Bajoran",))

rows = cursor.fetchall()

print("Bajoran Species' individuals:")
for name, age in rows:
    print(f"Name: {name}, Age: {age}")

conn.close()
