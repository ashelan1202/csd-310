import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "75292678",
    database = "movies"
)

cursor = db.cursor()

studio_records = ("SELECT studio_id, studio_name FROM studio")
cursor.execute(studio_records)
records_results = cursor.fetchall()
for x in records_results:
    print(x)

genre_records = ("SELECT genre_id, genre_name FROM genre")
cursor.execute(genre_records)
genre_results = cursor.fetchall()
for x in genre_results:
    print(x)

filmsRuntime = ("SELECT film_name FROM film WHERE film_runtime <= '120'")
cursor.execute(filmsRuntime)
runtime_results = cursor.fetchall()
for x in runtime_results:
    print(x)

filmDirectors = ("SELECT film_name, film_director FROM film ORDER BY film_director")
cursor.execute(filmDirectors)
directors_results = cursor.fetchall()
for x in directors_results:
    print(x)
