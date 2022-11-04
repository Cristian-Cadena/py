while True:

    x = int(input('Bienvenidos, por favor digita un numero del 1 - 1000: '))
    y = x % 2

    if x >= 1 and x <= 1000:
        if y == 0:
            print(f'El numero {x} es Par, presiona enter!!!\n')
            
        else:
            print(f'El numero {x} es Impar\n')
            
    else:
        print(f'Tu valor ingresado esta fuera del rango, digitalo nuevamente!!!\n')
    