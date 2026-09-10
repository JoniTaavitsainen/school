import mysql.connector


maakoodi = input("Anna maakoodi (esimerkiksi FI): ").upper()

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="",
)

kursor = yhteys.cursor()
kursor.execute(
    """
    SELECT type, COUNT(*)
    FROM airport
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
    """,
    (maakoodi,),
)

tulokset = kursor.fetchall()

if tulokset:
    for lentokenttatyyppi, lukumaara in tulokset:
        print(f"{lentokenttatyyppi}: {lukumaara}")
else:
    print("Maasta ei löytynyt lentokenttiä.")

kursor.close()
yhteys.close()