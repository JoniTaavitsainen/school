from math import isqrt

from flask import Flask, jsonify


app = Flask(__name__)


def onko_alkuluku(luku):
    if luku < 2:
        return False
    return all(luku % jakaja != 0 for jakaja in range(2, isqrt(luku) + 1))


@app.get("/alkuluku/<int:luku>")
def alkuluku(luku):
    return jsonify({"Number": luku, "isPrime": onko_alkuluku(luku)})


if __name__ == "__main__":
    app.run(port=3000)