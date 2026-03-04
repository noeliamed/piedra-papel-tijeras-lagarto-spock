# Juego: piedra, papel, tijeras, lagarto, Spock

import random
    
opciones = ['piedra', 'papel', 'tijeras', 'lagarto', 'Spock']

seguir = 's'

victorias_usuario = 0
victorias_ordenador = 0
empates = 0



while seguir == 's':

    ordenador = random.choice(opciones)

    eleccion = input('Elije una opción (piedra, papel, tijeras, lagarto, Spock): ')

    if eleccion == ordenador:
        print('Empate')
        empates += 1
    elif eleccion == 'piedra' and ordenador == 'tijeras':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'piedra' and ordenador == 'lagarto':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'tijeras' and ordenador == 'piedra':
        print('El ordenador gana')
        victorias_ordenador += 1
    elif eleccion == 'lagarto' and ordenador == 'piedra':
        print('El ordenador gana')
        victorias_ordenador += 1
    elif eleccion == 'papel' and ordenador == 'piedra':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'piedra' and ordenador == 'papel':
        print('El ordenador gana')
        victorias_ordenador += 1
    elif eleccion == 'piedra' and ordenador == 'Spock':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'Spock' and ordenador == 'piedra':
        print('El ordenador gana')
        victorias_ordenador += 1
    elif eleccion == 'tijeras' and ordenador == 'papel':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'papel' and ordenador == 'tijeras':
        print('El ordenador gana')
        victorias_ordenador += 1
    elif eleccion == 'tijeras' and ordenador == 'lagarto':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'lagarto' and ordenador == 'tijeras':
        print('El ordenador gana')
        victorias_ordenador += 1
    elif eleccion == 'lagarto' and ordenador == 'Spock':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'Spock' and ordenador == 'lagarto':
        print('El ordenador gana')
        victorias_ordenador +=1
    elif eleccion == 'lagarto' and ordenador == 'papel':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'papel' and ordenador == 'lagarto':
        print('El ordenador gana')
        victorias_ordenador +=1
    elif eleccion == 'Spock' and ordenador == 'tijeras':
        print('El usuario gana')
        victorias_usuario += 1
    elif eleccion == 'tijeras' and ordenador == 'Spock':
        print('El ordenador gana')
        victorias_ordenador += 1
    else:
        print('Ninguan de las anteriores')


    print('El usuario eligió:', eleccion)
    print('El ordenador eligió:',  ordenador)

    seguir = input('¿Quieres seguir jugando? (s/n): ')

    print('Marcador final: ')
    print('Usuario: ', victorias_usuario, ' | Ordenador: ', victorias_ordenador, ' | Empates: ', empates)
