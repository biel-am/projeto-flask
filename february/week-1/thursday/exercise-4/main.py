import psycopg2

connection = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='181044')

cursor = connection.cursor()

cursor.execute('SELECT * FROM film')

films = cursor.fetchall()

print(films)

cursor.close()
connection.close()
