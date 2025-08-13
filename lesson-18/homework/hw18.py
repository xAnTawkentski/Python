#homework2
#task1
import pandas as pd
df = pd.read_csv('stackoverflow_qa.csv')

# Sana ustunini datetime formatiga o'tkazish (masalan, ustun nomi 'CreationDate')
df['creationdate'] = pd.to_datetime(df['creationdate'])

# 2014-yil 1-yanvardan oldin yaratilgan savollarni tanlash
filtered_df = df[df['creationdate'] < '2014-01-01']

# Natijani ko'rish
print(filtered_df)


#task2
# 'score' ustunidan 50 dan katta bo‘lgan satrlarni tanlash
filtered_df = df[df['score'] > 50]

print(filtered_df)

#task3
filtered2 = df[df['score'].between(50,100)]
print(filtered2)

#task4
scott = df[df['ans_name']=='Scott Boston']
print(scott)

#task5
users = ['tatwright', 'DarkAnt', 'David Underhill', 'yueerhu', 'Jason Strimpel']

# Ushbu foydalanuvchilarning savollarini tanlash
questions_by_users = df[df['quest_name'].isin(users)]

print(questions_by_users[['id', 'quest_name', 'title']])


#task6
# Sana ustunini datetime formatga o‘tkazish
df['creationdate'] = pd.to_datetime(df['creationdate'])

# Filtrlash: 2014-03-01 dan 2014-10-31 oralig‘i, ans_name = 'unutbu', score < 5
filtered_df = df[
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'].str.lower() == 'unutbu') &
    (df['score'] < 5)
]

# Natijani ko‘rsatish
print(filtered_df[['id', 'creationdate', 'title', 'score', 'ans_name']])


#task7
# Shart bo‘yicha filtrlash
filtered_df = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) |
    (df['viewcount'] > 10000)
]

# Natijani chiqarish (asosiy ustunlar bilan)
print(filtered_df[['id', 'title', 'score', 'viewcount']])


#task8
# Scott Boston tomonidan javob BERILMAGAN savollarni tanlash
filtered_df = df[df['ans_name'] != 'Scott Boston']

# Natijani chiqarish
print(filtered_df[['id', 'title', 'ans_name']])

#Homework3:
#task1
import pandas as pd

# CSV faylni o'qish
titanic_df = pd.read_csv("titanic.csv")

# NaN qiymatlar bo'lishi mumkin, shuning uchun avval Age ustunini tozalaymiz
filtered_df = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].notna()) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]

# Natijani ko'rsatish
print(filtered_df[['PassengerId', 'Name', 'Age', 'Pclass', 'Sex']])


#task2
# Fare > 100 bo'lgan yo'lovchilarni tanlash
high_fare_df = titanic_df[titanic_df['Fare'] > 100]

# Natijani ko'rsatish (asosiy ustunlar bilan)
print(high_fare_df[['PassengerId', 'Name', 'Fare', 'Pclass']])

#task3
# Filtrlash
alone_survivors = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

# Natijani chiqarish
print(alone_survivors[['PassengerId', 'Name', 'Survived', 'SibSp', 'Parch']])


#task4
# Filtrlash
filtered_df4 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

# Natijani ko'rsatish
print(filtered_df4[['PassengerId', 'Name', 'Embarked', 'Fare']])


#task5
# Filtrlash
family_aboard = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

# Natijani ko'rsatish
print(family_aboard[['PassengerId', 'Name', 'SibSp', 'Parch']])

#task6
# Age ustunida NaN qiymatlar bo'lishi mumkin, shuning uchun oldin NaN qiymatlarni chiqaramiz
filtered_df6 = titanic_df[
    (titanic_df['Age'].notna()) &
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

# Natijani chiqarish
print(filtered_df6[['PassengerId', 'Name', 'Age', 'Survived']])

#task7
# Filtrlash
filtered_df7 = titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare'] > 200)
]

# Natijani ko'rsatish
print(filtered_df7[['PassengerId', 'Name', 'Cabin', 'Fare']])

#task8
# Toq sonli PassengerId larni tanlash
odd_id_df = titanic_df[titanic_df['PassengerId'] % 2 == 1]

# Natijani ko'rsatish
print(odd_id_df[['PassengerId', 'Name']])

#task9
# Har bir ticket nechta borligini hisoblash
ticket_counts = titanic_df['Ticket'].value_counts()

# Faqat 1 marta uchraydigan ticketlarni olish
unique_tickets = ticket_counts[ticket_counts == 1].index

# Ushbu unique ticketlarga ega yo'lovchilarni tanlash
unique_ticket_passengers = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]

# Natijani chiqarish
print(unique_ticket_passengers[['PassengerId', 'Name', 'Ticket']])

#task10
# Filtrlash
miss_class1_females = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Name'].str.contains('Miss'))
]

# Natijani ko'rsatish
print(miss_class1_females[['PassengerId', 'Name', 'Sex', 'Pclass']])


