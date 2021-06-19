class Operaciones():
    pi = 3.1415 
    def __init__(self, num1, num2):
        self.__numero1= num1
        self.__numero2= num2
    @property
    def numero1(self): 
        return self.__numero1
    @numero1.setter
    def numero1(self, valor):
        self.__numero1=valor 
    @property
    def numero2(self): 
        return self.__numero2
    @numero2.setter
    def numero2(self, valor): 
        self.__numero2=valor
    def suma(self):     
        resp= self.__numero1+ self.__numero2
        return resp
    def mostrar_Datos(self):
        print("La suma de: {}+{} es:{}".format(self.__numero1,self.__numero2,self.suma()))
ope1= Operaciones(2,4)
ope2= Operaciones(4,6)
print("La suma de: ", ope1.numero1, "+", ope1.numero2, "es: ", ope1.suma(), "," , "Valor de pi: ", ope1.pi)  
print("La suma de: ", ope2.numero1, "+", ope2.numero2, "es: ", ope2.suma(), "," , "Valor de pi: ", ope2.pi)    