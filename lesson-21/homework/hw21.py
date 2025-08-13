#DataFrame 1: Student Grades
import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

#task1
# Calculate average across subjects for each student
df1['Average_Grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# Display the updated DataFrame
print(df1)

#task2
# Agar Average_Grade hali hisoblanmagan bo‘lsa, hisoblaymiz
if 'Average_Grade' not in df1.columns:
    df1['Average_Grade'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# Eng yuqori o‘rtacha bahoga ega bo‘lgan o‘quvchini topamiz
top_student = df1.loc[df1['Average_Grade'].idxmax()]

print("Student with the highest average grade:")
print(top_student)


#task3
# Total ustunini qo‘shamiz
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

# Natijani ko‘rsatamiz
print(df1)


#task4

import matplotlib.pyplot as plt

# Har bir fan bo‘yicha o‘rtacha baholarni hisoblaymiz
subject_averages = df1[['Math', 'English', 'Science']].mean()

# Bar chart chizamiz
plt.figure(figsize=(8, 5))
plt.bar(subject_averages.index, subject_averages.values, color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average Grades per Subject')
plt.ylabel('Average Grade')
plt.ylim(0, 100)

# Baholarni ustiga yozib qo‘yamiz
for i, value in enumerate(subject_averages.values):
    plt.text(i, value + 1, f'{value:.1f}', ha='center')

plt.show()


#DataFrame 2: Sales Data
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

#task1
# Har bir mahsulot bo‘yicha jami savdoni hisoblash
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()

print("Total Sales for Each Product:")
print(total_sales)


#task2
# Har bir kun uchun jami savdoni hisoblaymiz
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)

# Eng yuqori umumiy savdo bo‘lgan sanani topamiz
max_sales_date = df2.loc[df2['Total_Sales'].idxmax()]

print("Date with the highest total sales:")
print(max_sales_date[['Date', 'Total_Sales']])

#task3
# Har bir mahsulot uchun kunlik o'zgarishni (foizda) hisoblaymiz
df2['Product_A_Change_%'] = df2['Product_A'].pct_change() * 100
df2['Product_B_Change_%'] = df2['Product_B'].pct_change() * 100
df2['Product_C_Change_%'] = df2['Product_C'].pct_change() * 100

# Natijani ko‘rsatamiz
print(df2[['Date', 'Product_A_Change_%', 'Product_B_Change_%', 'Product_C_Change_%']])



#task4
import matplotlib.pyplot as plt

# Chizma o‘lchami
plt.figure(figsize=(10, 6))

# Har bir mahsulot uchun chiziq chizamiz
plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='s')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='^')

# Grafik sarlavhasi va o‘qlari
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)  # Sanalarni burish
plt.legend()
plt.grid(True)
plt.tight_layout()

# Grafikni ko‘rsatish
plt.show()


#DataFrame 3: Employee Information
import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

#task1
# Har bir bo‘lim uchun o‘rtacha maoshni hisoblash
average_salary_by_dept = df3.groupby('Department')['Salary'].mean().round(2)

print("Average Salary by Department:")
print(average_salary_by_dept)



#task2
# Eng ko'p tajribaga ega xodimni topamiz
most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]

print("Employee with the most experience:")
print(most_experienced_employee)


#task3
# Minimal ish haqini topamiz
min_salary = df3['Salary'].min()

# Har bir xodim uchun minimal maoshga nisbatan foiz oshishni hisoblaymiz
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Natijani yaxshilab ko‘rsatish uchun yaxlitlaymiz
df3['Salary Increase (%)'] = df3['Salary Increase (%)'].round(2)

print(df3)



#task4
import matplotlib.pyplot as plt

# Har bir bo‘limdagi xodimlar sonini hisoblaymiz
dept_counts = df3['Department'].value_counts()

# Bar chart chizamiz
plt.figure(figsize=(8,5))
dept_counts.plot(kind='bar', color='skyblue')

plt.title('Number of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.show()


#DataFrame 4: Customer Orders
import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

#task1
# Jami daromadni hisoblash
total_revenue = df4['Total_Price'].sum()

print(f"Total Revenue from all orders: ${total_revenue}")

#task2
# Har bir mahsulot bo‘yicha jami buyurtma sonini hisoblaymiz
product_quantity = df4.groupby('Product')['Quantity'].sum()

# Eng ko'p buyurtma berilgan mahsulotni topamiz
most_ordered_product = product_quantity.idxmax()
most_ordered_quantity = product_quantity.max()

print(f"Most ordered product: {most_ordered_product} with total quantity {most_ordered_quantity}")


#task3
# Buyurtmalar bo‘yicha o‘rtacha mahsulot miqdorini hisoblash
average_quantity = df4['Quantity'].mean()

print(f"Average quantity of products ordered per order: {average_quantity:.2f}")

#task4
import matplotlib.pyplot as plt

# Har bir mahsulot bo‘yicha jami savdoni hisoblaymiz
sales_by_product = df4.groupby('Product')['Total_Price'].sum()

# Pie chart chizamiz
plt.figure(figsize=(7,7))
plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'salmon'])
plt.title('Sales Distribution by Product')
plt.axis('equal')  # Doira ko‘rinishi uchun

plt.show()






