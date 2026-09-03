def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa


luvut = [4, 6, 1, 9, 7, 8]
print(f"Listan {luvut} summa on {laske_summa(luvut)}.")