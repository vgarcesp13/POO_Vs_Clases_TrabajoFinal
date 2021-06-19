class Lista:
    def __init__(self, datos): #parametro es la variable que esta definidda en el metodo
        self.lista = datos
    def numeros_pares(self):
        pares = []
        for num in self.lista:
            if num %2==0:
                pares.append(num)
        return pares
    def vocales(self):
        
        vocales = {}
        cv=0
        for car in self.lista. lower():
            if car in("a", "e", "i", "o", "u"):
                cv=cv+1
        vocales["vocales"]= cv
        return vocales
    def cantidad_vocales(self):
        voc, cva, cve, cvi, cvo, cvu =  {}, 0, 0, 0, 0, 0
        for car in self.lista.lower():
            if car in ("a"):
                cva=cva+1
            elif car in ("e"):
                cve=cve+1
            elif car in ("i"):
                cvi=cvi+1
            elif car in ("o"):
                cvo=cvo+1
            elif car in ("u"):
                cvu=cvu+1
        voc["a"]=cva 
        voc["e"]=cve
        voc["i"]=cvi 
        voc["o"]=cvo
        voc["u"]=cvu
        return voc         
        
frase= "Hola que TAL como te va"
lista3 = Lista(frase)
dic= lista3.cantidad_vocales()
print(dic)
        
'''lista2 = Lista(frase)
diccionario= lista2.vocales()
print(diccionario) 

notas = [2,4,5,7,9,10,12]
lista1 = Lista(notas) #argumento que se envia cuando se invoca al metodo
print(lista1.lista,lista1.numeros_pares())
frase = "Hola;que;TAL"


#fraseLista= frase.split(";") #split separa por espacio 
#print(fraseLista)
#fr= ';'.join(fraseLista)
#print("fr= ",fr)'''