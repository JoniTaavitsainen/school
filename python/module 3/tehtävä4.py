import time


def on_karkausvuosi(vuosi):
    if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
        return True
    return False


def mainloop():
    try:
        vuosi = int(input("Anna vuosi: "))

        if on_karkausvuosi(vuosi):
            print(f"{vuosi} on karkausvuosi.")
        else:
            print(f"{vuosi} ei ole karkausvuosi.")

    except ValueError:
        print("Virheellinen syöte. Anna vain vuosiluku.")
        time.sleep(1)
        mainloop()


mainloop()
