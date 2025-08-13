#homework1
#task1

import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect('chinook.db')

# 1. Customer ma'lumotlarini olish
df_customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Customer", conn)

# 2. Invoice (to'lov) ma'lumotlarini olish
df_invoices = pd.read_sql_query("SELECT CustomerId, Total FROM Invoice", conn)

conn.close()

# 3. Har bir mijozning jami sarfini hisoblash
df_total_spent = df_invoices.groupby('CustomerId').agg(TotalSpent=('Total', 'sum')).reset_index()

# 4. Customer ma'lumotlari bilan birlashtirish (join)
df = pd.merge(df_total_spent, df_customers, on='CustomerId')

# 5. Jami sarflangan summaga ko'ra kamayish tartibida sort qilish va top 5 ni olish
top5_customers = df.sort_values(by='TotalSpent', ascending=False).head(5)

# 6. Natijani chiqarish (Customer ID, Ism, Familiya, Jami summa)
top5_customers = top5_customers[['CustomerId', 'FirstName', 'LastName', 'TotalSpent']]

print(top5_customers)



#task2
import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect('chinook.db')

# InvoiceLine, Track, Album, Customer ma'lumotlarini olish
invoice_lines = pd.read_sql_query("""
SELECT il.InvoiceId, il.TrackId, i.CustomerId
FROM InvoiceLine il
JOIN Invoice i ON il.InvoiceId = i.InvoiceId
""", conn)

tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)

albums = pd.read_sql_query("""
SELECT AlbumId, COUNT(*) as AlbumTrackCount
FROM Track
GROUP BY AlbumId
""", conn)

conn.close()

# InvoiceLine orqali qaysi treklar kim tomonidan olinganini bilamiz
# Track -> AlbumId ni ulaymiz
invoice_lines = invoice_lines.merge(tracks, on='TrackId', how='left')

# Endi mijozlar va ular xarid qilgan treklar to'plamini tahlil qilamiz
# Har bir mijoz-albom juftligi uchun u nechta trek olganini sanaymiz
customer_album_tracks = invoice_lines.groupby(['CustomerId', 'AlbumId']).agg(
    PurchasedTrackCount=('TrackId', 'count')
).reset_index()

# Har bir albomda nechta trek borligini qo'shamiz
customer_album_tracks = customer_album_tracks.merge(albums, on='AlbumId', how='left')

# Endi aniqlaymiz: mijoz barcha treklarni olganmi?
customer_album_tracks['FullAlbumPurchase'] = customer_album_tracks['PurchasedTrackCount'] >= customer_album_tracks['AlbumTrackCount']

# Har bir mijoz uchun toifani aniqlaymiz
def determine_preference(group):
    if all(group['FullAlbumPurchase']):
        return 'Full Albums'
    else:
        return 'Individual Tracks'

customer_preferences = customer_album_tracks.groupby('CustomerId').apply(determine_preference).reset_index()
customer_preferences.columns = ['CustomerId', 'Preference']

# Yakuniy statistikani chiqaramiz
summary = customer_preferences['Preference'].value_counts(normalize=True) * 100
summary = summary.round(2).reset_index()
summary.columns = ['Preference', 'Percentage']

print(summary)
