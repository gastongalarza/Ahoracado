#AHORCADO

palabra = input("Ingrese una palabra para adivinar: ")
vidas = 5
letras_restantes = list(palabra) #Letras restantes que le quedan por adivinar al jugador
letras_usadas = []

#Se determina la cantidad de espacios (con guion bajos) de la palabra
progreso = [] #Es el estado de la palabra a adivinar
for i in range(len(palabra)):
    progreso.append("_")
    
def verifica_gano_partida():
  return letras_restantes == []    

def agregar_letra(letra):
    letras_usadas.append(letra)

def mostrar_letras_usadas():
    print("Letras usadas: ", letras_usadas)

while vidas > 0:
    
    letra_ingresada = input("Introduce una letra: ")
    agregar_letra(letra_ingresada)

    if letra_ingresada not in palabra:
        vidas-=1
        print("NO ACERTASTE LA LETRA !")
           
    else:
     for i in range(len(palabra)): 
        if letra_ingresada == palabra[i]: #se ha acertado la letra
            progreso[i] = letra_ingresada #se actualiza el progreso
            letras_restantes.remove(letra_ingresada)

    if verifica_gano_partida() == True:
        print(progreso)
        print("FELICIDADES, GANASTE !!!")
        break

    
    print(progreso)
    print("Te quedan ",+vidas," vidas")
    mostrar_letras_usadas()
    
else:
    
    print("PERDISTE! :(")
    print("GRACIAS POR PARTICIPAR")