class Colecciones:
    def __init__(self,datos=[]):
        self.coleccion= datos
        
    def obtenerElemento(self):
        ele= self.coleccion[2]
        pri= self.coleccion[0]
        ult= self.coleccion[-1]
        ra1= self.coleccion[:2]
        ra2= self.coleccion[1:3]
        ra3= self.coleccion[-3:-1]
        inv= self.coleccion[::-1]
        print("{}".format(self.coleccion))
        print("{} {} {} {} {} {} {}".format(ele,pri,ult,ra1,ra2,ra3,inv))
    
    def getElemento(self,pos):
        if pos < len(self.coleccion):
            return self.coleccion[pos]
        else:
            return -1
    
    def recorrido(self):
        cad = ''
        for ele in self.coleccion:
            print(ele)
        
        longitud = len(self.coleccion)
        for ind in range(0,longitud):
            print(ind)
        
        for ind,ele in enumerate(self.coleccion):
            print(ind,ele)
            
        for ind in range (0,longitud):
            if ind == longitud-1:
                cad += self.coleccion[ind]
            else:
                cad += self.coleccion[ind]+","
        return cad
    
    def diccionario(self):
        dic2 = {}
        for clave,valor in self.coleccion.items():
            print(clave,":",valor)
            dic2[clave]= valor
        return dic2
    
    def invertirLista(self):
        return self.coleccion[::-1]
    
    def listaTupla(self):
        L1=[]
        for i in self.coleccion:
            L1+= tuple(i)
        return(L1)

        # usuarios= ' '
        # for usuario in self.coleccion:
        #     print(usuario)
        #     for dato in usuario:
        #         usuarios= usuarios+dato
        #     usuarios=usuarios+' '
    
    def listaDiccionario(self, valor1):
        Cad= ""
        for i in valor1:
            if i not in (" ","{","}"):
                Cad+= i
        x= Cad.split(",")
        return(x)
        
    def listaComprehension(self, fra):
        lista = [car for car in fra if car in ('a','e','i','o','u')]
        return lista
    
    def diccioComprehension(self):
        dic= { numero:numero**2 for numero in range(1,11) if numero%2==0}
        print (dic)
        frase = 'Hola que tal,como te va,mi gran amigo'
        resp={',':pos for pos,car in enumerate(frase) if car==','}
        print(resp)
        return[dic,resp]
    
        # cad = 'casa1,3,5'
        # c=0
        # caracter = 's'
        # lista=[]
        # for pos in range (0,len(cad)):
        #     ele = cad[pos]
        #     if ele == caracter:
        #         lista.append(pos)
        # print(lista)


# col = Colecciones()
# col.diccioComprehension()
        
# #valor = "Hola que tal"
# #lista = valor.split()
# print (lista)
# col= Colecciones(lista)
# #col.obtenerElemento()
# p = col.getElemento(3)
# print(p)
# #print(col.getElemento(1))
# print(col.recorrido())

#col=Colecciones({'nombre':'Daniel','edad':'52'})
#print(col.diccionario())

# valor= "nom:Daniel,edad:50"
# lista = valor.split(',')
# print(lista)
# dic={}
# for item in lista:
#     pos= item.find(":")
#     clave= item[:pos]
#     valor= item[pos+1:]
#     dic[clave]=valor
# col = Colecciones(dic)   
# print(col.diccionario())

#PERFECTO
# c,ac=1,0
# while c < num:
#     if num%c == 0:
#         ac=ac + c
# return ac

# #PRIMO
# def primo(self,num):
#     c=2
#     pri = True
#     while c < num:
#         if num%c == 0:
#             pri =False
#             break
#         else:
#             c=c+1
#     return pri 

#AMIGOS 

