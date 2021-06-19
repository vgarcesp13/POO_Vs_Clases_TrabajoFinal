class Cadena:
    def __init__(self,cad): #metodo constructor
        self.__cadena = cad
    @property #metodo property
    def cadena(self):
        return self.__cadena
    def longitud(self): #Método longitud
        lon=len(self.__cadena)
        return lon
    
    def mostrar(self):  #Método mostrar
        print("La cadena '{}' tiene: {} caracteres".format(self.__cadena,self.longitud()))

class Caracteres(Cadena):
    def __init__(self,cad):
        super().__init__(cad)
    def posicion(self):
        
        palab= input("Ingrese la palabra que desea buscar: ")
        if palab in self.cadena:
           return self.cadena.index(palab)
        else:
           return (-1)    
    def Buscar(self,cad):
        posiciones=[]
    buscar=0

    while buscar != -1:
        buscar=cad.find(buscar)
        if posicion !=-1:
            posiciones.append(posicion)
            posicion+=1
    return posiciones


cad = 'Hola que tal, que haces'
subc = 'que'
posiciones = posicion(cad, subc)
print('Posiciones:', posiciones)

   
    
    def eliminar(self):
        sub=input("Ingrese que la palabra que desea eliminar: ")
        nombre= ["Hola", "que",  "tal", "que", "haces"]
        nombre.remove(sub)
        return nombre
        
    def mostrar_dat(self):
        super().mostrar()
        print("La frase es: {}".format(self.cadena))
        print("La posicion de la palabra buscada es: {}".format(self.posicion()))        
        print("La palabra eliminada es: {}".format(self.eliminar()))
               
variable= ("Hola como estas, como te encuentras")
subc= "como"
fra= Caracteres(variable)
fra.mostrar_dat()
#metodo len se aplica a las cadenas