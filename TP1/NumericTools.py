import numpy as np
import math


#################BISECCION######################
def biseccion(f, a, b,tol=1):
    """ Se ingresa la funcion f la cual recibe un numero y devuelve un numero, los limites del intervalo
    y el error absoluto porcentual. Devuelvo la raiz de la funcion f en el intervalo [a,b]"""
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    it_num = calculate_eBiseccion(a, b, tol)
    return _biseccion(f, a, b, (a+b)/2.0, it_num)


def _biseccion(f, a, b, x, it):
    if it <= 0:
        return x
    if np.sign(f(a)) * np.sign(f(x)) > 0:
        a = x
    else:
        b = x
    return _biseccion(f, a, b, (a+b)/2.0, it-1)


def calculate_eBiseccion(a, b, tol=1):
    tol = tol/100
    it_num = np.log2((b-a)/tol)
    return it_num


def secante(a, b, tol = 1):
    pass

#####################PUNTO FIJO ##############################


def punto_fijo(g,semilla,max_iteraciones=100,e=0.01):
    i=0
    x=semilla
    while (i<max_iteraciones):
        x1=g(x)
        error=abs(x1-x)
        #print(i,x1,error)
        if (error<e):
            return x1
        i=i+1
        x=x1
    return "Error"