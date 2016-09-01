__author__ = 'Rodrigo'
def downtriangle(filas, contEspacios=0):
    if filas == 0:
        return 0
    else:
        print('  ' * ( contEspacios + 1 ) + '* ' * ( filas * 2 - 1 ))
        return downtriangle( filas - 1, contEspacios + 1 )

