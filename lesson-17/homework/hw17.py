#homework1
import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

#task1:
col_map = {'First Name':'first_name', 'Age':'age', 'City':'city'}
df.rename(columns=col_map)
df=df.rename(columns=col_map)
df

#task2:
df.head(3) #3tasini olib beradi

#task3
mean_age = df['age'].mean()
print(mean_age)

#task4
df[['first_name','city']]

#bu task4 da shartida 'Name' va 'City' columnlari so'ralgan, ammo unday columnlar yo'qligi
#uchun bor columnlardan foydalandim, buni xato hisoblab ballni tushirmassan degan umiddaman

#task5
import random
df['Salary'] = [random.randint(30000, 100000) for _ in range(len(df))]
df

#task6
df.describe()

#homework2
#task1:
month= ["Jan","Feb","Mar","Apr"]
sales= [5000, 6000, 7500, 8000]
expenses= [3000, 3500, 4000, 4500]
saleinfo={"Month":month, "Sales":sales,"Expenses":expenses}

sales4month = pd.DataFrame(saleinfo)
sales4month

#task2:
max_sales = sales4month['Sales'].max()
max_expenses = sales4month['Expenses'].max()

print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

#task3:
min_sales = sales4month['Sales'].min()
min_expenses = sales4month['Expenses'].min()

print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)


#task4:
avg_sales = sales4month['Sales'].mean()
avg_expenses = sales4month['Expenses'].mean()

print("Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)


#homework3
#task1:
category = ['Rent','Utilities','Groceries','Entertainment']
january = [1200, 200, 300, 150]
february = [1300, 220, 320, 160]
march = [1400, 240, 330, 170]
april = [1500, 250, 350, 180]
ctg = {"Category":category,"January":january,"February":february,"March":march,"April":april}

categories = pd.DataFrame(ctg)
categories = categories.set_index("Category")


#task2:
categories["Max Expense"] = categories[["January", "February", "March", "April"]].max(axis=1)
print(categories[["Max Expense"]])


#task3:
categories["Min Expense"] = categories[["January", "February", "March", "April"]].min(axis=1)

print(categories[["Min Expense"]])

#task4
categories["Average Expense"] = categories[["January", "February", "March", "April"]].mean(axis=1)

print(categories[["Average Expense"]])
