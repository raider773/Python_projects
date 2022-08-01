import random

numero = random.randint(1,100)


n = int(input("Guess the number between 1 and 100 : "))

#validamos

while n < 1 or n > 100:
    print("Out Of Bounds")
    n = int(input("Guess the number: "))

#primer intento
if n == numero:
        print("you fucking won")
        print("you tried 1 times")
        



while n != numero:
     
    if n < numero - 10 or n > numero + 10:
        print("cold")
    else:
        print("warm")


#distancia_primer_numero

    if n < numero:
        distancia = numero - n
    elif n > numero:
        distancia = n - numero



#ComparoDistanciaPrimerNumConElSeg

    n = int(input("Guess the number: "))
    while n < 1 or n > 100:
        print("Out Of Bounds")
        n = int(input("Guess the number: "))
    if n == numero:
        print("you fucking won")
        print("you tried 2 times")
        break
    
    

    if n < numero:
            distancia1 = numero - n
    elif n > numero:
            distancia1 = n - numero

    if distancia1 < distancia:
        print("warmer")
    else:
        print("colder")

#ElLoopDeLasGuess

    cont = 2

    while n != numero:    
        n = int(input("Guess the number: "))
        while n < 1 or n > 100:
            print("Out Of Bounds")
            n = int(input("Guess the number: "))


        if n < numero:
            distancia = numero - n
        elif n > numero:
            distancia = n - numero
        cont = cont + 1 


        if n == numero:
            break

        elif distancia < distancia1:
            print("warmer")
        
        else:
            print("colder")

        distancia1 = distancia

    print("you won")
    print("you tried {} times".format(cont))
    input()
        
    





    

    
    

    

        
    
    
    
    
