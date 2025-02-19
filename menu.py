while True:

    #mostramos un menú
    print("--> ( Menú Calculadora 📠) <--\n")
    print("=====================================")
    print("\n1. Sumar")
    print("\n2. Restar")
    print("\n3. Multiplicar")
    print("\n4. Dividir")
    print("\n5. Salir\n")
    print("\n--> Seleccione una opción: ")
    print("=====================================")

    #leemos la opción del usuario

    opcion = input("ingrese una opción: ")

    #verificamos si la opción es válida

    if opcion == "1":
        print("\n--> Sumar <--\n")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("\nEl resultado de la suma es: ", num1 + num2)
    elif opcion == "2":
        print("\n--> Restar <--\n")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("\nEl resultado de la resta es: ", num1 - num2)
    elif opcion == "3":
        print("\n--> Multiplicar <--\n")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("\nEl resultado de la multiplicación es: ", num1 * num2)
    elif opcion == "4":
        print("\n--> Dividir <--\n")
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("\nEl resultado de la división es: ", num1 / num2)
    elif opcion == "5":
        print("\n--> Saliendo del programa <--\n")
        break
    else:  
        print("\n--> Opción no válida <--\n")
        print("\n--> Por favor, seleccione una opción válida <--\n")
        break

