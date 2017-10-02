import numpy as np


def biseccion(f, a, b, tol = 1):
    """ Se ingresa la funcion f la cual recibe un numero y devuelve un numero, los limites del intervalo
    y el error absoluto porcentual. Devuelvo la raiz de la funcion f en el intervalo [a,b]"""
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")

    return _biseccion(f, a, b, tol, (a+b)/2.0)


def _biseccion(f, a, b, tol, x):
    if calculate_eBiseccion(a,b) < tol:
        return x
    if np.sign(f(a)) * np.sign(f(x)) > 0:
        a = x
    else:
        b = x
    return _biseccion(f, a, b, tol, (a+b)/2.0)

def calculate_eBiseccion(a,b):
    return ((b-a)/2)*100

def secante(f, a, b, tol = 1):
    c = b - a