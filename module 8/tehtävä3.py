import mysql.connector
from geopy.distance import geodesic


ensimmainen_koodi = input("Anna ensimmäisen lentoaseman ICAO-koodi: ").upper()
toinen_koodi = input("Anna toisen lentoaseman ICAO-koodi: ").upper()

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
    SELECT ident, latitude_deg, longitude_deg
    FROM airport
    WHERE ident IN (%s, %s)
    """,
    (ensimmainen_koodi, toinen_koodi),
)

koordinaatit = {rivi[0]: (rivi[1], rivi[2]) for rivi in kursor.fetchall()}

if ensimmainen_koodi in koordinaatit and toinen_koodi in koordinaatit:
    etaisyys = geodesic(
        koordinaatit[ensimmainen_koodi],
        koordinaatit[toinen_koodi],
    ).kilometers
    print(f"Lentoasemien välinen etäisyys on {etaisyys:.1f} kilometriä.")
else:
    print("Jompaakumpaa lentoasemaa ei löytynyt.")

kursor.close()
yhteys.close()