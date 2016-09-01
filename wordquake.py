__author__ = 'Rodrigo'
def wordquake (palabra):
    palabraconvertida = ''
    cont = 0
    for letra in palabra:
        if cont%2 == 0:
            var = letra.upper()
        else:
            var = letra.lower()

        palabraconvertida = palabraconvertida+var
        cont +=1

    print (palabraconvertida)

wordquake('Weird string case')