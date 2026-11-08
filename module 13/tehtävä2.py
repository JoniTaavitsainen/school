import mysql.connector
from flask import Flask, jsonify


app = Flask(__name__)


def hae_lentoasema(icao_koodi):
    yhteys = mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="",
    )
    try:
        kursor = yhteys.cursor()
        try:
            kursor.execute(
                """
                SELECT name, municipality
                FROM airport
                WHERE ident = %s
                """,
                (icao_koodi,),
            )
            return kursor.fetchone()
        finally:
            kursor.close()
    finally:
        yhteys.close()


@app.get("/kenttä/<string:icao_koodi>")
def kentta(icao_koodi):
    icao_koodi = icao_koodi.upper()
    try:
        tulos = hae_lentoasema(icao_koodi)
    except mysql.connector.Error:
        app.logger.exception("Lentoasematietokannan kysely epäonnistui.")
        return jsonify({"error": "Lentoasematietokannan kysely epäonnistui."}), 500

    if tulos is None:
        return jsonify({"error": "Lentoasemaa ei löytynyt."}), 404

    return jsonify(
        {
            "ICAO": icao_koodi,
            "Name": tulos[0],
            "Municipality": tulos[1],
        }
    )


if __name__ == "__main__":
    app.run(port=3000)