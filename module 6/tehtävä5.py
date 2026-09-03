def karsi_parittomat(luvut):
    parilliset_luvut = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset_luvut.append(luku)
    return parilliset_luvut


luvut = [1, 2, 3, 4, 5, 6, 7, 8]
karsittu_lista = karsi_parittomat(luvut)

print(f"Alkuperäinen lista: {luvut}")
print(f"Karsittu lista: {karsittu_lista}")