

abecedario = {'a' : [],
              'b' : [],
              'c' : [],
              'd' : [],
              'e' : [],
              'f' : [],
              'g' : [],
              'h' : [],
              'i' : [],
              'j' : [],
              'k' : [],
              'l' : [],
              'm' : [],
              'n' : [],
              'o' : [],
              'p' : [],
              'q' : [],
              'r' : [],
              's' : [],
              't' : [],
              'u' : [],
              'v' : [],
              'w' : [],
              'x' : [],
              'y' : [],
              'z' : []}
              
              



def acomodar_juegos (abecedario,linea):
    for letra in abecedario:
        if linea[0].lower() == letra:
            linea = linea.rstrip()
            abecedario[letra].append(linea)

def mostrar_letra (abecedario):
    print('')
    letra = input("Que letra desea buscar: ")
    letra = letra.strip()
    print('')
    if letra.lower() in abecedario:
        for juego in abecedario[letra]:
            print('                                                         ○',juego.capitalize())
            print('')
    else:
        print('letra no valida')
        
def mostrar_tabla(abecedario):
    print('')
    for letra in abecedario:
        print ('                                                            ',letra.capitalize(),)
        print(' ')
        for juego in abecedario[letra]:
            print('                                                        ○',juego.capitalize())
            print('')

        
def preguntar_letra_o_tabla():
    print('Quiere Ver tabla completa o buscar por letra?') 
    rta = input("Por favor escriba 'tabla' o letra': ")
    rta = rta.strip()
    while True:
        if rta.lower() == 'tabla':
            opcion = 'a'
            break
        elif rta.lower() == 'letra':
            opcion = 'b'
            break
        else:
            print('Opcion no valida')
        rta = input("Por favor escriba 'tabla' o letra': ")
    return opcion

def borrar_repes_lista (lista):
    lista1 = lista    
    listabuena = []
    for x in lista1:
        if x not in listabuena:
            listabuena.append(x)
    return listabuena
   
    
      

#creo diccionario  

original = open(r"C:\Juegos\Juegos Jugados.txt")

linea = original.readline()

while linea:
    acomodar_juegos (abecedario,linea)    
    linea = original.readline()

original.close()

#borrar repetidos y ordenar

for letra in abecedario:
     abecedario[letra] = borrar_repes_lista (abecedario[letra])
     abecedario[letra].sort()


#mostrar tabla o letra
    
opcion = preguntar_letra_o_tabla()

if opcion == 'a':
    mostrar_tabla(abecedario)
elif opcion == 'b':
    mostrar_letra (abecedario)
    
while True:
    print('')
    print('Desea realizar otra operacion?')
    rta = input('si o no: ')
    rta = rta.strip()
    if rta == 'no':
        break
    elif rta == 'si':
        opcion = preguntar_letra_o_tabla()

        if opcion == 'a':
            mostrar_tabla(abecedario)
        elif opcion == 'b':
            mostrar_letra (abecedario)
    else:
        print('escriba si o no')

print('Ponete a estudiar vago')
input()
    
    
    







