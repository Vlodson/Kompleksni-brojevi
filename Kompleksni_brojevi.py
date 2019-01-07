""" mesto za importovanje """
import numpy as np
import math
import matplotlib.pyplot as plt

#----------------------------

""" Klasa kompleksnih brojeva:
    X 1) kada se inicijalizuje potrebno je napisati realni i imaginarni deo
    X 2) pozivom oblik metode se printuju svi oblici kompleksnih brojeva (algebarski, magnituda i ugao, trig oblik, ojlerov oblik)
       algebarski = x+yi | magn i ugao = |z|<arctan(teta) | trig = |z|(cos(teta + isin(teta))) | ojler = |z|e^iteta (msm da ovo nije oblik provericu)
    X 3) moze da radi sve racunske operacije (+,-,*,/,^) (postoje division by zero i NaN-ovi)
    4) moze da graficki prikaze tacke
    5) moze da graficki prikaze funkcije"""


""" da bi se napravio kompleksni broj u konzolu se pise: ime_var = Cplx(realni_deo, imaginarni_deo), gde su argumenti brojevi i ne pise se i """
""" sve racunske operacije vracaju Cplx(real, im) """
class Cplx():

    """ funkcija za plotovanje kompleksnih brojeva (dodati jos arg za other.im i real jer imas samo za self.im i real i treba ti jos arg za real i im koje funkc vraca)"""
    def plot_cplx(realni_deo, imaginarni_deo):

        """ ime x i y ose """
        x_osa_label = plt.xlabel('Realna osa')
        y_osa_label = plt.ylabel('Imaginarna osa')
        plt.grid()

        """ velicina grafika da uvek bude skalirana nvm"""
        #plt.axis([realni_deo - 1, realni_deo + 1, imaginarni_deo - 1, imaginarni_deo + 1])

        """ plotuje jedinicni krug  |  x = +-1/koren iz 1 + tan na kv teta , teta = [1,360]  |  y = +-tan teta / koren iz 1 + tan na kv teta, teta = [1,360]
            na istu foru su izracunate i koord za korenje samo umesto 1/ je |z| / """
        x = []
        y = []

        for i in range(1,360):
            x.append(1 / (1 + np.tan(math.radians(i))**2)**0.5) # +x
            x.append(-1 / (1 + np.tan(math.radians(i))**2)**0.5) # -x
            y.append(np.tan(math.radians(i)) / (1 + np.tan(math.radians(i))**2)**0.5) # +y
            y.append(-np.tan(math.radians(i)) / (1 + np.tan(math.radians(i))**2)**0.5) # -y

        plt.plot(x, y, 'b,')
        plt.plot(realni_deo, imaginarni_deo, c = 'b', marker='o')
        plt.plot([0,realni_deo], [0,imaginarni_deo], 'b-')

        plt.show()

    #-----------------------------------------------

    """ za inicijalizaciju kompleksnog broja """
    def __init__(self,real,im):
        self.real = real
        self.im = im

    #-----------------------------------------------

    # sin,cos,tan,ctg -> math.radians(f) daje radiane | arcf -> math.degrees(arcf) daje stepene
    def oblik(self, graph = False):
        magnituda = round(((self.real**2 + self.im**2)**0.5),2) # mogu ovo da stavim kao globalnu promenljivu u klasi ali iskreno nije nikakvo cimanje napisati pitagoru kada treba
        ugao = round(math.degrees(np.arctan(self.im/self.real)),2) # isto kao ovo gore, doduse mi ne treba uvek ovaj math.degrees deo
        print("Algebarski oblik je: {}+({}*i)".format(self.real, self.im))
        print("Magnituda i ugao su: {} <{}".format(magnituda, ugao))
        print("Trigonometrijski oblik je: {}(cos{} + i*sin{})".format(magnituda, ugao, ugao))
        print("Ojlerov oblik je: {}*e^(i*{})".format(magnituda, ugao))

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)

    #-----------------------------------------------

    """ (real1 + real2) + (im1 + im2)i """
    def sabiranje(self, other, graph = False):
        real = self.real + other.real
        im = self.im + other.im

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)
            Cplx.plot_cplx(other.real, other.im)
            Cplx.plot_cplx(real, im)

        return Cplx(real, im)

    #-----------------------------------------------

    """ (real1 - real2) + (im1 - im2)i """
    def oduzimanje(self, other, graph = False):
        real = self.real - other.real
        im = self.im - other.im

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)
            Cplx.plot_cplx(other.real, other.im)
            Cplx.plot_cplx(real, im)

        return Cplx(real, im)

    #-----------------------------------------------

    """ u(x+yi) = ux +uyi """
    def mnozenje_const(self, const, graph = False):
        real = self.real * const
        im = self.im * const

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)
            Cplx.plot_cplx(real, im)

        return Cplx(real, im)

    #-----------------------------------------------

    """ (x1+y1i)(x2+y2i) = (x1*x2 - y1*y2) + (x1y2 + y1x2)i """
    def mnozenje_dva_C(self, other, graph = False):
        real = self.real*other.real - self.im*other.im
        im = self.real*other.im + self.im*other.real

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)
            Cplx.plot_cplx(other.real, other.im)
            Cplx.plot_cplx(real, im)

        return Cplx(real, im)

    #-----------------------------------------------

    """ (x+yi)/u = x/u + (y/u)i """
    def deljenje_const(self, const, graph = False):
        real = self.real / const
        im = self.im / const

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)
            Cplx.plot_cplx(real, im)


        return Cplx(real,im)

    #-----------------------------------------------

    """ (x1+y1i)/(x2+y2i) = (x1x2 + y1y2)/(x2^2 + y2^2) + ((x2y1 - x1y2)/(x2^2 + y2^2))i"""
    def deljenje_dva_C(self, other, graph = False):
        real = (self.real*other.real + self.im*other.im) / (other.real**2 + other.im**2)
        im = (self.im*other.real - self.real*other.im) / (other.real**2 + other.im**2)

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)
            Cplx.plot_cplx(other.real, other.im)
            Cplx.plot_cplx(real, im)

        return Cplx(real,im)

    #-----------------------------------------------

    """ samo loopujem mnozenje ali sam sa sobom (za ovo nemas grafik, nzm ni kako da ga ubacim)"""
    def stepenovanje(self, deg):
        i = 0
        for i in range(deg):
            return Cplx.mnozenje_dva_C(self, self)

    #-----------------------------------------------

    """ n-ti koren = |z|^(1/n) * (cos(teta + 2kpi)/n + i*sin(teta+2kpi)/n) koreni se obicno racunaju za 0 do n """
    def koren(self, deg, graph = False):
        magnituda = round(((self.real**2 + self.im**2)**.5)**(1/deg), 2)
        ugao = round(math.degrees((np.arctan(self.im/self.real)+2*(deg-1)*math.pi)/deg), 2)

        """ formulu sam izveo na papiru, sustina je da postoji samo jedna tacka sa tom magnitudom i uglom pa odatle proizilaze ove dve (mozda fali +- negde tokom racuna) """
        real = round(magnituda / ((1 + np.tan(ugao)**2)**.5), 2)
        im = round(magnituda * np.tan(ugao) / ((1 + np.tan(ugao)**2)**.5), 2)

        if graph == True:
            Cplx.plot_cplx(self.real, self.im)
            Cplx.plot_cplx(real, im)

        return Cplx(real, im)

    #-----------------------------------------------
