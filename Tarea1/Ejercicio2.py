#EJERCICIO 2
def fibonacci(cantidad):
    a = 0
    b = 1
    suma = 0
    contador_div = 1
    div = 0
    for i in range(cantidad):
        suma = a + b
        a = b
        b = suma
        for i in range(1,b):
            div = b % i
            if div == 0:
                contador_div += 1
        if contador_div > 1000:
            print("El numero {} tiene mas de mil divisores".format(b))
            break
        else:
            contador_div = 0
        print('{}'.format(suma))
fibonacci(120)