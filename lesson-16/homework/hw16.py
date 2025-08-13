#task1
# Import NumPy kutubxonasi
import numpy as np

# Asl ro'yxat
original_list = [12.23, 13.32, 100, 36.32]
print("Original List:", original_list)

# Ro'yxatni 1D NumPy massivga aylantirish
array = np.array(original_list)
print("One-dimensional NumPy array:", array)


#task2
import numpy as np

# 2 dan 10 gacha bo'lgan qiymatlar bilan 3x3 matritsa yaratish
matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)


#task3
import numpy as np

# 10 ta elementdan iborat null (0) vektor yaratish
vector = np.zeros(10)
print("Original null vector:")
print(vector)

# Oltinchi qiymatni 11 ga yangilash (indeks 6)
vector[6] = 11
print("\nUpdate sixth value to 11:")
print(vector)


#task4
import numpy as np

# 12 dan 38 gacha bo'lgan qiymatlar bilan massiv yaratish (38 kirmaydi)
array = np.arange(12, 38)
print(array)


#task5
import numpy as np

# Asl massiv (int tipida)
original_array = np.array([1, 2, 3, 4])
print("Original array:", original_array)

# Float tipiga o'zgartirish
float_array = original_array.astype(float)
print("Array converted to float type:", float_array)


#task6
import numpy as np

# Centigrade qiymatlar (Selsiy bo‘yicha)
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
print("Values in Centigrade degrees:", celsius)

# Celsius to Fahrenheit formulasi: F = (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print("Values in Fahrenheit degrees:", fahrenheit)


#task7
import numpy as np

# Asl massiv
original_array = np.array([10, 20, 30])
print("Original array:", original_array)

# Qo'shiladigan qiymatlar
values_to_append = [40, 50, 60, 70, 80, 90]

# Append qilish
updated_array = np.append(original_array, values_to_append)
print("After append values to the end of the array:", updated_array)


#task8
import numpy as np

# 0 dan 100 gacha bo'lgan 10 ta tasodifiy butun sonli massiv
array = np.random.randint(0, 100, 10)
print("Random Array:", array)

# Statistik hisob-kitoblar
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)


#task9
import numpy as np

# 10x10 o'lchamdagi tasodifiy float qiymatlar massivi (0 dan 1 gacha)
array = np.random.random((10, 10))
print("Random 10x10 Array:\n", array)

# Minimum va maksimum qiymatlar
min_value = np.min(array)
max_value = np.max(array)

print("\nMinimum value in array:", min_value)
print("Maximum value in array:", max_value)


#task10
import numpy as np

# 3x3x3 o'lchamdagi tasodifiy float qiymatlar massivi (0 dan 1 gacha)
array_3d = np.random.random((3, 3, 3))
print("3x3x3 Random Array:\n", array_3d)
