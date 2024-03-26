# Un asesor nos ha solicitado un programa para calcular los pagos mensuales de una hipoteca, de manera que pueda asesorar a sus clientes sobre ello. El programa debe solicitar el capital del prestamo (c), el interes anual (i) y el número de años (n) de la hipoteca y debe escribir la cuota a pagar mensualmente. Para calcular esta cuota se utiliza la siguiente formula, donde R es el interes mensual:

def calcular_cuota_mensual(capital, interes_anual, años):
    interes_mensual = interes_anual / 12 / 100

    num_pagos = años * 12

    cuota_mensual = (capital * interes_mensual) / (1 - (1 + interes_mensual) ** -num_pagos)

    return cuota_mensual

capital = float(input("Ingrese el capital del préstamo: "))
interes_anual = float(input("Ingrese el interés anual: "))
años = int(input("Ingrese el número de años: "))
cuota = calcular_cuota_mensual(capital, interes_anual, años)
print("La cuota mensual a pagar es:", cuota)
