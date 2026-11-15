import os
import sys
from getpass import getpass

import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"


def hae_saa(paikkakunta, api_avain):
    vastaus = requests.get(
        API_URL,
        params={
            "q": paikkakunta,
            "appid": api_avain,
            "lang": "fi",
        },
        timeout=10,
    )
    vastaus.raise_for_status()
    tieto = vastaus.json()

    lampotila_kelvineina = tieto["main"]["temp"]
    lampotila_celsiuksina = lampotila_kelvineina - 273.15
    kuvaus = tieto["weather"][0]["description"]
    return kuvaus, lampotila_celsiuksina


def main():
    api_avain = "49991e095fed86066ca87c54306a817d"
    if not api_avain:
        print("API-avain ei voi olla tyhjä.", file=sys.stderr)
        return 1

    paikkakunta = input("Anna paikkakunta: ").strip()
    if not paikkakunta:
        print("Paikkakunta ei voi olla tyhjä.", file=sys.stderr)
        return 1

    try:
        kuvaus, lampotila = hae_saa(paikkakunta, api_avain)
    except requests.HTTPError as virhe:
        print(
            f"Säätietojen hakeminen epäonnistui ({virhe}). "
            "Tarkista paikkakunta ja API-avain.",
            file=sys.stderr,
        )
        return 1
    except (requests.JSONDecodeError, KeyError, IndexError) as virhe:
        print(f"Rajapinnan vastausta ei voitu käsitellä: {virhe}", file=sys.stderr)
        return 1
    except requests.RequestException as virhe:
        print(f"Yhteys säärajapintaan epäonnistui: {virhe}", file=sys.stderr)
        return 1

    print(f"Sää: {kuvaus}")
    print(f"Lämpötila: {lampotila:.1f} °C")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())