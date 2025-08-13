#Assignment1:
#task1

import pandas as pd

# CSV faylni o'qish
sales_df = pd.read_csv('sales_data.csv')
# Category bo'yicha guruhlash va kerakli statistikalarni hisoblash
category_stats = sales_df.groupby('Category').agg({
    'Quantity': ['sum', 'max'],    # jami sotilgan miqdor va eng katta sotuv
    'Price': 'mean'                # o'rtacha narx
})

# Kolonkalarni yaxshiroq nomlash
category_stats.columns = ['Total Quantity Sold', 'Max Quantity Sold in One Transaction', 'Average Price per Unit']

# Natijani ko'rsatish
print(category_stats)

#task2
# Har bir category va product uchun jami Quantity ni hisoblash
category_product_qty = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

# Har bir category bo'yicha eng ko'p sotilgan mahsulotni topish
top_selling_products = category_product_qty.loc[
    category_product_qty.groupby('Category')['Quantity'].idxmax()
].reset_index(drop=True)

print(top_selling_products)

#task3
# Har bir satr uchun jami summani hisoblash
sales_df['TotalSale'] = sales_df['Quantity'] * sales_df['Price']

# Sana bo'yicha jami savdolarni hisoblash
daily_sales = sales_df.groupby('Date')['TotalSale'].sum()

# Eng yuqori jami savdo bo‘lgan sanani topish
max_sales_date = daily_sales.idxmax()
max_sales_amount = daily_sales.max()

print(f"Eng yuqori savdo summasi {max_sales_amount} bo‘lgan sana: {max_sales_date}")


#tAssignment2:
#task1
import pandas as pd

# CSV faylni o'qish
orders_df = pd.read_csv('customer_orders.csv')

# Har bir CustomerID uchun buyurtmalar sonini hisoblash
orders_count = orders_df.groupby('CustomerID')['OrderID'].nunique().reset_index(name='OrderCount')

# 20 va undan ko'p buyurtma bergan mijozlarni tanlash
customers_20_plus = orders_count[orders_count['OrderCount'] >= 20]

# Asl jadvaldan faqat 20 yoki undan ko'p buyurtma bergan mijozlarni chiqarish
filtered_orders_df = orders_df[orders_df['CustomerID'].isin(customers_20_plus['CustomerID'])]

# Natijani ko'rsatish
print(filtered_orders_df)



#task2
# Har bir mijoz bo'yicha o'rtacha narxni hisoblash
avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean().reset_index()

# Narxi 120 dan katta bo'lgan mijozlarni filtrlaymiz
high_spenders = avg_price_per_customer[avg_price_per_customer['Price'] > 120]

print(high_spenders)


#task3
# Har bir satr uchun jami summani hisoblash
orders_df['TotalPrice'] = orders_df['Quantity'] * orders_df['Price']

# Har bir mahsulot bo‘yicha jami Quantity va jami Price ni hisoblash
product_summary = orders_df.groupby('Product').agg({
    'Quantity': 'sum',
    'TotalPrice': 'sum'
}).reset_index()

# Jami Quantity 5 dan kam bo‘lgan mahsulotlarni chiqarib tashlash
filtered_products = product_summary[product_summary['Quantity'] >= 5]

print(filtered_products)

#Assignment3
#task2

import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect(r'population.db')

# population jadvalidan ma'lumotni olish
df_population = pd.read_sql_query("SELECT * FROM population", conn)

# Excel fayldan Salary Band kategoriyalarini o'qish
salary_bands = pd.read_excel(r'task\population salary analysis.xlsx')

# salary_bands faylida qanday ustunlar borligini bilish uchun:
print(salary_bands.columns)

# Misol uchun salary_bands faylida 'Salary Band', 'Min Salary', 'Max Salary' ustunlari bor deb faraz qilamiz
# Endi har bir odamni qaysi salary bandga kirishini aniqlaymiz

def assign_salary_band(salary):
    for _, row in salary_bands.iterrows():
        if row['Min Salary'] <= salary <= row['Max Salary']:
            return row['Salary Band']
    return 'Unknown'

df_population['Salary Band'] = df_population['salary'].apply(assign_salary_band)

# Har bir Salary Band uchun kerakli statistikalar:
total_population = len(df_population)

result = df_population.groupby('Salary Band').agg(
    Population_Count=('salary', 'count'),
    Average_Salary=('salary', 'mean'),
    Median_Salary=('salary', 'median')
).reset_index()

result['Percentage'] = (result['Population_Count'] / total_population) * 100

print(result)

conn.close()


#task3
import sqlite3
import pandas as pd

# 1. Bazadan faqat kerakli ustunlarni olamiz (state va salary)
conn = sqlite3.connect(r'population.db')
query = "SELECT state, salary FROM population"
df = pd.read_sql_query(query, conn)
conn.close()

# 2. Excel dan Salary Band kategoriyalarini o‘qiymiz
salary_bands = pd.read_excel(r'task\population salary analysis.xlsx')

# 3. Salary Band funksiyasi
def assign_salary_band(salary):
    for _, row in salary_bands.iterrows():
        if row['Min Salary'] <= salary <= row['Max Salary']:
            return row['Salary Band']
    return 'Unknown'

# Salary Band ustunini qo‘shamiz
df['Salary Band'] = df['salary'].apply(assign_salary_band)

# 4. Har bir State va Salary Band bo‘yicha guruhlab hisoblash
total_population = len(df)

result = df.groupby(['state', 'Salary Band']).agg(
    Population_Count=('salary', 'count'),
    Average_Salary=('salary', 'mean'),
    Median_Salary=('salary', 'median')
).reset_index()

# Foiz ulushini hisoblaymiz (har bir guruh aholisi / jami aholisi)
result['Percentage'] = (result['Population_Count'] / total_population) * 100

print(result)




