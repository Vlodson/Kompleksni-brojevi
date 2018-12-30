""" mesto za importovanje """
import numpy as np
import math

#----------------------------

""" Klasa kompleksnih brojeva:
    X 1) kada se inicijalizuje potrebno je napisati realni i imaginarni deo
    X 2) pozivom oblik metode se printuju svi oblici kompleksnih brojeva (algebarski, magnituda i ugao, trig oblik, ojlerov oblik)
       algebarski = x+yi | magn i ugao = |z|<arctan(teta) | trig = |z|(cos(teta + isin(teta))) | ojler = |z|e^iteta (msm da ovo nije oblik provericu)
    3) moze da radi sve racunske operacije (+,-,*,/,^) (ostalo je jos korenovanje) (postoje division by zero i NaN-ovi)
    4) moze da graficki prikaze tacke
    5) moze da resava funkcije"""

class Cplx():

    def __init__(self,real,im):
        self.real = real
        self.im = im

    # sin,cos,tan,ctg -> math.radians(f) daje radiane | arcf -> math.degrees(arcf) daje stepene
    def oblik(self):
        magnituda = round(((self.real**2 + self.im**2)**0.5),2)
        ugao = round(math.degrees(np.arctan(self.im/self.real)),2)
        cos_ugao = round(math.degrees(np.arccos(self.real/magnituda)),2)
        sin_ugao = round(math.degrees(np.arcsin(self.im/magnituda)),2)
        print("Algebarski oblik je: {}+({}*i)".format(self.real, self.im))
        print("Magnituda i ugao su: {} <{}".format(magnituda, ugao))
        print("Trigonometrijski oblik je: {}(cos{} + i*sin{})".format(magnituda, cos_ugao, sin_ugao))

    """ (real1 + real2) + (im1 + im2)i """
    def sabiranje(self,other):
        real = self.real + other.real
        im = self.im + other.im
        return Cplx(real, im)

    """ (real1 - real2) + (im1 - im2)i """
    def oduzimanje(self,other):
        real = self.real - other.real
        im = self.im - other.im
        return Cplx(real, im)

    """ u(x+yi) = ux +uyi """
    def mnozenje_const(self, const):
        real = self.real * const
        im = self.im * const
        return Cplx(real, im)

    """ (x1+y1i)(x2+y2i) = (x1*x2 - y1*y2) + (x1y2 + y1x2)i """
    def mnozenje_dva_C(self, other):
        real = self.real*other.real - self.im*other.im
        im = self.real*other.im + self.im*other.real
        return Cplx(real, im)

    """ (x+yi)/u = x/u + (y/u)i """
    def deljenje_const(self,const):
        real = self.real / const
        im = self.im / const
        return Cplx(real,im)

    """ (x1+y1i)/(x2+y2i) = (x1x2 + y1y2)/(x2^2 + y2^2) + ((x2y1 - x1y2)/(x2^2 + y2^2))i"""
    def deljenje_dva_C(self,other):
        real = (self.real*other.real + self.im*other.im) / (other.real**2 + other.im**2)
        im = (self.im*other.real - self.real*other.im) / (other.real**2 + other.im**2)
        return Cplx(real,im)

    """ samo loopujem mnozenje ali sam sa sobom """
    def stepenovanje(self, deg):
        i = 0
        for i in range(deg):
            return Cplx.mnozenje_dva_C(self, self)
