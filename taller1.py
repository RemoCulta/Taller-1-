Numero_uno = float(input("Escribe el primer numero: "))
Numero_Dos = float(input("Escribe el segundo numero: "))

opcion = 0 
while True: 
    print ("""
           ¿Que operacion matematica quieres hacer?
           1) Suma
           2) Resta
           3) Multiplicacion
           4) Divicion
           5) Salir 
           
           """)
    opcion = int(input("Elige una opccion: "))
    if opcion == 1:
        print (" ")
        print ("Resultado: La suma de", Numero_uno  ,"+",Numero_Dos, "es igual a", Numero_uno + Numero_Dos)
    elif opcion == 2:
        print(" ")
        print ("Resultado: La resta de", Numero_uno  ,"-",Numero_Dos, "es igual a", Numero_uno - Numero_Dos)
    elif opcion == 3:
        print(" ")
        print ("Resultado: El producto de ", Numero_uno  ,"*",Numero_Dos, "es igual a", Numero_uno * Numero_Dos)
    elif opcion == 4:
        print("")
        print ("Resultado: La divicion  de", Numero_uno  ,"/",Numero_Dos, "es igual a", Numero_uno / Numero_Dos)
    elif opcion==5:
        break
    else: 
        print("opccion invalida")