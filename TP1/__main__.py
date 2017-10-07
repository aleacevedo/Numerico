import Analytics as an
import NumericTools as nt


def punto2():
    analytics = an.Analytics()
    raiz = nt.biseccion(analytics.calculate_van, 0, 2)
    return raiz

def punto3():
    analytics = an.Analytics()
    semilla = nt.biseccion(analytics.calculate_van, 0, 2)
    raiz = nt.punto_fijo(analytics.g_van,semilla)
    return raiz


def __main__():
    print("Punto2: ")
    print(punto2())
    print("van:" + str(an.Analytics().calculate_van(punto2())))
    print("Punto3: ")
    print(punto3())
    print("van:" + str(an.Analytics().calculate_van(punto3())))

__main__()