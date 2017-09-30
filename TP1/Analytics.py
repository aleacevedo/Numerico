PI = 300            #Potencia a Instalar [KWpico]
CU = 1800           #Costo Unitario [usd/KWpico]
IG = 35             #Impuesto a las ganancias [%]
CE = 1.9            #Cargo de electricidad [$/KWh]
CP = 250            #Cargo de potencia [$/KW.mes]
TC = 17.50          #Tipo de cambio [$/usd]
N = 20              #Vida util del proyecto [anios]
P = 99146           #Padron
YH = 8760           #Year Hours [horas]
FR = 0.3            #Factor de reduccion de potencia contratada [%]
CO = 5000/TC        #Costos [usd/anio]
NE = 0              #Años de excepcion impositiva


class Analytics:

    def __init__(self, pi=PI, cu=CU, ig=IG, ce=CE, cp=CP, fr=FR, ne = NE):
        self.pi = pi
        self.cu = cu
        self.ig = ig
        self.ce = ce
        self.cp = cp
        self.fr = fr
        self.ne = ne
        self.io = self.calculate_I0()
        self.fu = self.calculate_FU()
        self.savesE = self.calculate_savesE()
        self.savesP = self.calculate_savesP()
        self.saves = self.calculate_saves()

    def calculate_I0(self):
        """ Devuleve la inversion inicial [usd]"""
        return (self.pi*self.cu)

    def calculate_FU(self):
        """ Devuelve el factor de uso [%]"""
        return ((0.18*P)/100000)

    def calculate_savesE(self):
        """ Devuelve los ahorros electricos en dolares"""
        return (self.pi*YH*self.fu*self.ce)/TC

    def calculate_savesP(self):
        """ Devuelven los ahorros de potencia en dolares"""
        return (self.pi*self.fr*self.cp*12)/TC

    def calculate_saves(self):
        """ Devuelven los ahorros totales en dolares"""
        return ((self.savesE)+(self.savesP))

    def calculate_fcf(self, excento=False):
        """ Ingresa True en caso de ser un año excento de impuestos.
        Devuleve el flujo de fondos en dolares"""
        if(excento): return (self.calculate_saves() - CO)
        return ((self.saves - CO)*(1+(self.ig/100)))

    def calculate_van(self, i):
        """ Ingresa la tasa de interes y devuelve el van"""
        aux = 0
        for x in range(1, self.ne+1):
            aux = aux + (self.calculate_fcf(True)/pow(1+i, x))
        for x in range(self.ne+1, N-self.ne+1):
            aux = aux + (self.calculate_fcf()/pow(1+i, x))
        return self.io - aux
