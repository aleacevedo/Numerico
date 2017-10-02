import Analytics as an
import NumericTools as nt


def punto2():
    analytics = an.Analytics()
    raiz = nt.biseccion(analytics.calculate_van, 0, 2)
    print(raiz)

def __main__():
    print("Punto2: ")
    punto2()

__main__()