class Operaciones():
    #constructor
    pi = 3.1415 #atributos de clases
    def __init__(self, num1, num2): #primer metodo que se instancia
        #atributos de instancia, su valor depende de cada instancia
        self.__numero1= num1
        self.__numero2= num2
    @property
    def numero1(self): #metodo getter (retorna valor del atributo privado)
        return self.__numero1
    @numero1.setter
    def numero1(self, valor): #metodo setter (asignar un valor a una variable)
        self.__numero1=valor
    @property
    def numero2(self): #metodo getter (retorna valor del atributo privado)
        return self.__numero2
    @numero2.setter
    def numero2(self, valor): #metodo setter 
        self.__numero2=valor
    #para accesar a privado crear un metodo property
    def suma(self):     
        resp= self.__numero1+ self.__numero2
        return resp
    '''def resta(self):
        #if (self.numero1 >= self.numero2):
        return self.numero1-self.numero2
    def multiplicacion(self):     
        return self.numero1*self.numero2
    def division(self):
        return self.numero1//self.numero2
    def divisionEntera(self):     
        return self.numero1+self.numero2
    def residuo(self):
        return self.numero1%self.numero2
    def exponente(self):     
        return self.numero1**self.numero2'''
    def mostrar_Datos(self):
        print("La suma de: {}+{} es:{}".format(self.__numero1,self.__numero2,self.suma()))
        #print("La resta de: {}-{} es:{}".format(self.numero1,self.numero2,self.resta()))
        #print("La multiplicacion de: {}*{} es:{}".format(self.numero1,self.numero2,self.multiplicacion()))
        #print("La division de: {}/{} es:{}".format(self.numero1,self.numero2,self.division()))
        #print("La divisionEntera de: {}//{} es:{}".format(self.numero1,self.numero2,self.divisionEntera()))
        #print("El residuo de: {}%{} es:{}".format(self.numero1,self.numero2,self.residuo()))
        #print("El exponente de: {}**{} es:{}".format(self.numero1,self.numero2,self.exponente()))                                      
#Herencia: la subclase hereda todos los atributos y metodos de la clase
'''class Ejercicio(Operaciones): #herencia, hereda una clase a partir de la existente
            #herencia sirve para crear cosas en otra clase herendando la anterior
    def __init__(self, n1, n2): #constructor de la subclase
        super().__init__(n1, n2) #ejecutar el constructor de la otra clase, una clase que hereda, hereda todo de la otra clase/clase padre
    def multiplicar(self, num1,num2):
        return num1*num2
    def tablaMultiplicar(self, num):
        con= 1
        resp= 0
        while con <= 12:
           resp= self.multiplicar(num, con)
           print("{}*{}={}".format(num, con,resp ))
           con= con+1
    def mostrar_Datos(self): #metodo mostrar de la subclase! clase derivada
        super().mostrar_Datos() #llama al metodo mostrar de la clase padre   
        print("___________________")
ope= Operaciones(2,4)       
ope.mostrar_Datos

ejer = Ejercicio(2,5) #instancia la clase y crea el objeto 
ejer.mostrar_Datos()
ejer.tablaMultiplicar(3)'''
#polimorfismo: cambiar el comportamiento d eun metodo de clase padre a clase hijo
#format un metodo string 
#self.variable es variable global en el metodo constructor
# # #self para que accese a las variables
#instancia= crear un objeto ope con los atributos y metodos de la clase operacion
#cuando se instancia se crea el objeto(en este caso ope) y se ejecuta el metodo
# constructor de la clase que estan en el constructor #metodos de la clase operacion
#ope.numero1 = 23 #asignar un valor a un atributo\
#ope.numero2 = ope.numero1
#print(ope.numero1, ope.numero2)#presenta valores de atributos
#para accesar a los atributos y metodos de los objetos instanciados
#ope= Operaciones(4,3) #instancia la clase, crea el objeto(ope)
#ope.mostrar_Datos()
#ope = Operaciones(2,4)
#print(ope.numero2) 
ope1= Operaciones(2,4)
ope2= Operaciones(4,6)
print("La suma de: ", ope1.numero1, "+", ope1.numero2, "es: ", ope1.suma(), ope1.pi)  
print("La suma de: ", ope2.numero1, "+", ope2.numero2, "es: ", ope2.suma(), ope2.pi)    
#property metodo especial que permite que el atributo sea extraido de otro atributo
#La función incorporada super() permite invocar un método de una clase padre desde una clase hija. herencia