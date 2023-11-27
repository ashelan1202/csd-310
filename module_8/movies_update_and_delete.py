import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "75292678",
    database = "movies",
)

cursor = db.cursor()

def show_films(cursor, title):
    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")

#cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

new_film = (
    "INSERT INTO film (film_name, film_director, film_releaseDate, film_runtime, studio_id, genre_id)" 
    "VALUES (%s, %s, %s, %s, %s, %s)"
) 
new_info = ('Coraline', 'Henry Selick', '2009', '100', 4, 1) 

new_studio = (
    "INSERT INTO studio(studio_id, studio_name)"
    "VALUES (%s, %s)"
)
new_studio_info = [4, 'LAIKA Films']

cursor.execute(new_studio, new_studio_info)
cursor.execute(new_film, new_info)
updated_movies = cursor.fetchall()

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

alien_update = "UPDATE genre SET genre_name = 'Horror' WHERE genre_name = 'SciFi'"
cursor.execute(alien_update)
updated_alien = cursor.fetchall()

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

bye_gladiator = "DELETE FROM film WHERE film_name = 'Gladiator'"
cursor.execute(bye_gladiator)
no_gladiator = cursor.fetchall()

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER REMOVAL")

