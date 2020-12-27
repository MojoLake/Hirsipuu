import random

lista = [("k", "i", "s", "s", "a"), ("j", "a", "l", "k", "a", "p", "a", "l", "l", "o"),
         ("a", "s", "u", "n","t", "o")]
sanalista = ["kissa", "jalkapallo", "asunto"]


a = random.randint(0, 2)

sana = lista[a]
def sana_arvaus_kisa():
    uusisana = ""
    hidword = ""
    x = 0
    for i in sana:
        hidword = hidword + "_"
    while x != 1:


        print("Vihje: " + hidword)

        sanavaikirjain = input("Haluatko arvata sanaa vai kirjainta? 0 jos sanaa, 1 jos kirjainta: ")

        if sanavaikirjain == "0":
            sana_arvaus = input("Arvaa sanaa: ")
            if sana_arvaus == sanalista[a]:
                print("Oikein meni, voitit!")
                x = 1
            else:
                print("Väärin meni")


        if sanavaikirjain == "1":
            kirjain_arvaus = input("Arvaa kirjainta: ")
            if kirjain_arvaus in lista[0]:
                for kirjain in lista[0]:
                    if kirjain_arvaus == kirjain:
                        uusisana = uusisana + kirjain
                    else:
                        uusisana = uusisana + "_"
                        hidword = uusisana
            else:
                print("Ei ole")


        print(uusisana)

sana_arvaus_kisa()



