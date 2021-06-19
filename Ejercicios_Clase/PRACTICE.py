class Numero:
    def __init__ (self, num):
        self.numero=num #objetivo del constructor, inicializar los atributos de la clase
    def Par_Impar (self):  
        #rec= self.numero  
        return self.numero %2==0
        # if self.numero %2==0:
        #     print("El numero {} que ingreso: es par".format(self.numero))
        # else: 
        #     print("El numero {} que ingreso: es impar".format(self.numero))
    def Lista(self):
        lista=[]
        con, limit, acu= 0,10,0
        while con<limit:
            acu= acu+self.numero
            if self.numero %2==0:
                print("El numero {} : Es par".format(self.numero))
            else:
                print("El numero {} : Es impar".format(self.numero))
        
        
numero= int(input("ingrese un numero: "))
ejer1= Numero(numero)
ejer1.Par_Impar()
if ejer1== True:
    print("par")
else:
    print("Impar")
    