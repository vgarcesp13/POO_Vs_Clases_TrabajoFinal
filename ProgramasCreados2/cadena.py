class Cadenas:
    def __init__(self,cadena=None):
        self.frase= cadena
        
    def recorrer(self):
        lista=[car for car in self.frase]
        return lista
    
    def invertir(self):
        return self.frase[::-1]
    
    def buscar(self,car):
        c=0
        long = len(self.frase)
        lista = []
        while c < long:
            if car == self.frase[c]:
                lista.append(c)
            c=c+1
        return lista[0]
    
    def ocurrencia(self,car):
        c=0
        long = len(self.frase)
        lista = []
        while c < long:
            if car == self.frase[c]:
                lista.append(c)
            c=c+1
        return car
            
    def vocalesCadena(self,voc):
        return [voc for voc in self.frase if voc in ('a','e','i','o','u')]
    
    def cadena_lista(self):
        fras = self.frase
        frasc = fras.split()
        return frasc

    def BuscarSub(self,subca):
            c=0
            long = len(self.frase)
            lista = []
            lo=len(subca)
            while c < long:
                if subca[0] == self.frase[c] and subca ==self.frase[c:c+lo]:
                    lista.append(c)
                c=c+1
            return lista
        
    def reempla(self,pala):
        cade= self.frase.replace('a',pala,)
        return cade
    
    def insertSubcadena(self,pln):
        c=0
        long = len(self.frase)
        lista = []
        lo=len(pln)
        while c < long:
            if pln[0] == self.frase[c] and pln==self.frase[c:c+lo]:
                 lista.append(c)
            c=c+1
        return lista
    def Convertir(self):
        lista = [self.frase]
        list = "".join(lista)
        return list
        
    def concatenar(self,carc):
        return (self.frase + ""+ carc)
    
    
        