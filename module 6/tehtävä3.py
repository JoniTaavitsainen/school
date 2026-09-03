def gallonat_litroiksi(gallon):
    return gallon * 3.785


while True:
    gallon = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))

    if gallon < 0:
        break

    print(f"{gallon} gallonaa on {gallonat_litroiksi(gallon)} litraa.")