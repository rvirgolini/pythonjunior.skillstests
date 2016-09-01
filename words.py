__author__ = 'Rodrigo'
def init(ubicacion):
    archivo = open(ubicacion,"r")
    palabras = []
    for line in archivo:
        for word in line.split():
            var = contar_consonantes(word)
            if var > 2:
                palabras.append(word)

    print(palabras)

def contar_consonantes(word):
    cant=0
    for letra in word:
        if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
            cant +=1
    return cant

init("C:/Users/Rodrigo/Desktop/palabras.txt")