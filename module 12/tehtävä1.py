import requests


API_URL = "https://api.chucknorris.io/jokes/random"


def hae_satunnainen_vitsi():
    vastaus = requests.get(API_URL, timeout=10)
    vastaus.raise_for_status()
    return vastaus.json()["value"]


if __name__ == "__main__":
    try:
        print(hae_satunnainen_vitsi())
    except (requests.JSONDecodeError, KeyError) as virhe:
        print(f"Rajapinnan vastausta ei voitu käsitellä: {virhe}")
    except requests.RequestException as virhe:
        print(f"Vitsin hakeminen epäonnistui: {virhe}")