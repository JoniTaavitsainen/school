oikea_kayttaja = "python"
oikea_salasana = "rules"

yritykset = 0

while yritykset < 5:
    kayttaja = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if kayttaja == oikea_kayttaja and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yritykset += 1
        if yritykset == 5:
            print("Pääsy evätty")
        else:
            print("Väärät tunnukset. Yritä uudelleen.")
