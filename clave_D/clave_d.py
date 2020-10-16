import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
numero1 = 2
numero2 = 4
numero3 = 3
def multiplicar(numero1, numero2, numero3):
    producto = numero1*numero2*numero3
    return producto


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    a = 1000
    suma = 0
  while a<=2000
     div3 = i%3
     div5 = i%5
   if div3 == 0 and div5 == 0
        suma +=a
        a+=1
   else
        a+=1
    result = suma  
 return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(longitud, latitud, altura)
     longitud = 10
     latitud = 6
     altura = 5
    obtenerArea()
    obtenerVolumen()


def obtenerArea():
    definicionOrtoedro()
    result = 2(longitud · latitud + longitud · altura + latitud · altura)
    return result


def obtenerVolumen():
    definicionOrtoedro()
    result = longitud · latitud · altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def definicionOrtoedro(self, longitud, latitud, altura): 
        self.lonitud = longitud
        self.latitud = latitud
        self.altura = altura
        
    def areaOrtoedro (self):
        result = 2(longitud · latitud + longitud · altura + latitud · altura)
    return result

    def volumenOrtoedro (self):
        result = longitud · latitud · altura
    return result
        


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
https://github.com/baylagas/py-parcial-q3-2020/edit/master/clave_D/clave_d.py
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
