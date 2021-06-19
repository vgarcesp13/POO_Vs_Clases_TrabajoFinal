class Cadena:
    def __init__(self,cad):
        self.__cadena = cad
        
    @property
    def cadena(self):
        return self.__cadena
    def longitud(self):
        longi = len(self.__cadena)
        return longi
    def mostrarCadena(self):
        print ("Cadena '{}' tiene: {} letras".format(self.cadena,self.longitud()))
        
class palabras(Cadena):
    def __init__(self,cad):
        super().__init__(cad)
        
    def buscPalabra(self):
        palabra = input("Ingrese la palabra que va a buscar: ")
        if palabra in self.cadena:
            return self.cadena.find(palabra)
        else:
            return(-1)
    def mostrar(self):
       super().mostrarCadena()   
       print("la palabra a buscar es: {}".format(self.buscPalabra()))
frase = "Hola como estas"
pal = palabras(frase)
pal.mostrar()