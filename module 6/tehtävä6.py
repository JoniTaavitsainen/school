import math


def pizzan_yksikkohinta(halkaisija_cm, hinta_euroina):
    sade_metreina = halkaisija_cm / 100 / 2
    pinta_ala = math.pi * sade_metreina ** 2
    return hinta_euroina / pinta_ala


halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

yksikkohinta1 = pizzan_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = pizzan_yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta on {yksikkohinta1:.2f} €/m².")
print(f"Toisen pizzan yksikköhinta on {yksikkohinta2:.2f} €/m².")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzat antavat yhtä hyvän vastineen rahalle.")