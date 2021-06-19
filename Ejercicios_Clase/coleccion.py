#Clase Coleccion
class Coleccion:
    #Definición del constructor
    def __init__(self, datos=[1,3,5]): #inicializar los atributos que va a tener la clase
        self.coleccion=datos 
    def Obtener_Ellemento(self):
        ele= self.coleccion[2]
        pri= self.coleccion[0]
        ult= self.coleccion[-1]
        ra1= self.coleccion[:2]
        ra2= self.coleccion[1:3]
        ra3= self.coleccion[-3:-1]
        inv= self.coleccion[::-1]
        print("{}".format(self.coleccion))
        print("{}--{}--{}--{}--{}--{}".format(ele,pri,ult,ra1,ra2,ra3, inv))
    def recorrido(self):
        #Elemento
        for ele in self.coleccion:
            print(ele)
        longitud = len(self.coleccion)
        #Posición
        for indice in range(0,longitud):
            print(indice)
        #Elemento y posición
        for indice,ele in enumerate(self.coleccion):
            if indice %2 ==0 and indice !=0 :
                print(indice, "--> ", ele)
    def diccionario(self):
        #items lo mismo que enumerate pero es para diccionario
        dic2={}
        for clave, valor in self.coleccion.items(): 
            print(clave, "-->" ,valor)
        aux= self.coleccion
        #Modificar una variable
        aux["edad"]= 21
        #Añadir una variable
        aux["Instructor"]= "Cargo"
        dic2["Empleado"]= "Freddy"
        dic2["sueldo"]=500
        print(aux,dic2)
        #print(dic2)
#instancia de la clase coleccion
#Se crea el objeto lista q posee todos los atributos metodos
# de la clase Colecciones y ejecuta el constructor
#de cla clase Colecciones; creando el atributo coleccion
'''lista= Coleccion(['Hola', 123, 50, True])
#print(lista.coleccion)
#lista.coleccion.append("Amigo")
#lista.coleccion.reverse()
#print(lista.Obtener_Ellemento())'''
'''tupla=Coleccion((20,40,60,80,100))
tupla.Obtener_Ellemento()
print(tupla.coleccion)
tupla.recorrido()
#print(tupla.coleccion [::-1])'''
dic= Coleccion({"Nombre":"Verónica", "edad":"20", "Estudiante": True})
dic.diccionario()

