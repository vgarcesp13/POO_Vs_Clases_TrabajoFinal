class Ejercicio:
    def __init__(self,num):
        self.dato=num
    def parImpar(self):
        acu= 0
        rec= self.dato  % 2
        if rec== 0:
            print("El numero: {} es Par ".format(self.dato))
        else:
            print("El numero: {} es Impar ".format(self.dato))
    def imparpar(self, numero):
        rec= numero % 2
        return rec
    def SumaPar(self,lista):
        c, ac=0,0
        lim=len(lista) #limite de la lista len obtiene cantidad
        for c in range(lim): #range, rango de valores
            num = lista[c]
            if self.imparpar(num) ==0:
                ac= ac+num #incremento
        print("La suma de los numeros pares de la lista: {} es = {} ".format(lista, ac))
    def VerificaPositivo(self):
        num= -1
        lista= []
        while num <0:
            num= int(input("Ingrese numero: "))
            lista.append(num)
        lista.pop()
        print("El numero que ingreso : {} es positivo y los almacenados son: {} ".format(num, lista))    
    def presentarFrase (self, frase):
        c, lim= 0, len(frase)  
        for c in range (lim): #(0,14)
            print(frase[c])
    def presentarFrase2(self,frase):
        for car in frase: 
            print(car)
    #def presentarFrase2(self,)
            
#ejer1= Ejercicio(9)
# ejer1.parImpar()
# resp = ejer1.imparpar(8)
# if resp ==0:
#     print("Par")
# else:
#     print("impar")
# lis = [2,4,5,1,6,8,14,2,6,4]
# print(lis[4:6])
# #una lista es un arreglo que esta compuesta or una seccion de elemento

# ejer1.VerificaPositivo()
# #while para condiciones sin incrementos, for para incrementos, para con contadores """
ejer3 = Ejercicio() #creando variable de tipo frase, si no se pasa el constructor le pone 0 
cade = "Hola"
tupla = ("daniel", 50, "M", True)
lista = [2,5,8,10]
ejer3.presentarFrase(cade)
ejer3.presentarFrase(tupla)
ejer3.presentarFrase(lista)