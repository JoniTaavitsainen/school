import mysql.connector


icao_koodi = input("Anna lentoaseman ICAO-koodi: ").upper()

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="",
)

kursor = yhteys.cursor()
kursor.execute(
    "SELECT name, municipality FROM airport WHERE ident = %s",
    (icao_koodi,),
)
tulos = kursor.fetchone()

if tulos:
    print(f"Lentoasema: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("Lentoasemaa ei löytynyt.")

kursor.close()
yhteys.close()