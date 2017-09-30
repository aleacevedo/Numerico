import numpy as np


def biseccion(f, a, b, tol = 1.0e-3):
    """ Se ingresa la funcion f la cual recibe un numero y devuelve un numero
    y los limites del intervalo. Devuelvo la raiz de la funcion f en el intervalo [a,b]"""
    if a > b:
        raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")

    return _biseccion(f, a, b, tol, (a+b)/2.0)


def _biseccion(f, a, b, tol, x):
    if b-a < tol:
        print(x)
        return x
    if np.sign(f(a)) * np.sign(f(x)) > 0:
        a = x
    else:
        b = x
    return _biseccion(f, a, b, tol, (a+b)/2.0)