valor = 0
while True:
    print("""seleccione opcion
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- dividir 
        """)

    valor = int(input("Elige una opcion: ") )     
    num1 = int(input("numero 1: ")) 
    num2 = int(input("numero 2: ")) 
    if valor == 1:
        print("la suma es: ",num1+num2)
        break
    if valor == 2:
        print("la resta es: ",num1-num2)
        break
    if valor == 3:
        print("la multiplicacion es: ",num1*num2)
        break
    if valor == 4:
        if num2 == 0:
            print("No se puede dividir por 0")
        elif num2 >= 1:
            print("la division es: ",num1/num2)
            break
        

    else:
        print("Opcion incorrecta")
        break