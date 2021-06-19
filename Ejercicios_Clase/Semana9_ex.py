class Ejercicios:
        
    def Ejer1(self):
        number= 3
        if number %2==0:
            print("El numero que ingreso : {}, es par ".format(number))
        else:
            print("El numero que ingreso: {}, es impar".format(number))
    
    def Ejer4(self):
        n1,n2,n3= 2,5,7
        if (n1>n2 and n1>n3):
            print("El numero: {}, es mayor".format(n1))
        elif (n2>n1 and n2>n3):
            print("El numero: {}, es mayor".format(n2))     
        else:
            print("El numero: {}, es mayor".format(n3))
    
    def Ejer7(self):
        salir= False
        acu= 0
        while salir== False:
            n= int(input("Ingrese un numero: "))
            if n <0:
                salir= True
            else: 
                acu+=n
        print(acu)
    
    def Ejer10(self):
        acum= 1
        aux= 0
        Salir= False
        while Salir == False:
            n= input("Ingrese un numero o presione F para salir: ")
            if n == "F":
                Salir= True
                Acum= None
            else:
                n= int(n)
                acum*= n
                aux= acum
        print(aux)
                
    def Ejer13(self):
        acum= 0
        num=2
        lista=[]
        while num<30:
            lista+=[num]
            if num%5 == 0:
                acum+=num
            num+=3
        print(lista)
        print(acum) 
        
    def Ejer16(self):
        acu,numero,con,= 0,1,0
        while numero >0:
            numero= int(input("Ingrese un numero: "))
            if numero %2!=0:
                con= con+numero
            else:
                acu= acu+numero
        print(acu)
   
    def Ejer19(self):
        con= 0
        num= int(input("Ingrese un número: "))
        for i in range(2, num):
            if num % i==0: 
                con+=1
        if con !=2:
            print( num, "Es primo")
        else:
            print(num, "No es primo")
                    
    def Ejer22(self):
        x, num, numeros, con,acu= 1,0,0,0,1
        num=(int(input("Ingrese el total de numero a calcular: ")))
        for x in range(num):
            numeros= int(input("Ingrese un número: "))
            if numeros %2==0:
                con= con+numeros
            if numeros %5== 0:
                acu= acu*numeros 
        print(con,acu)
  
    def Ejer25(self):
        mayor,ind,cont=0,0,0
        num= []
        for i in range (1,5):
            i=int(input("Ingrese un numero: "))
            num+=[i]
            if i>mayor :
             mayor=i
             ind=cont
            cont=cont+1 
        print("Los números ingresados son: ",num) 
        print("La posicion del numero mayor es: ", ind)
      
    def Ejer28(self):
        num= [2,4,6,3]
        print("El vector A es: ", num)
        num.sort()
        print("Números en orden: ",num)
  
    def Ejer31(self):
        numero= [4,5,6,3,7,8,0,1,5,6,7,3,12,6,25,13,9,31,16,33]
        print("Vector: ", numero)
        numero.sort() 
        print("Vector ordenado: ", numero) 
        
    def Ejer34(self, M= [[11, 3, 5], [7, 9, 0], [4, 6, 10]]):
        Mayor= None
        Menor= None
        PMax= []
        PMin= []
        for i in range(len(M)):
            for j in range(len(M[i])):
                if (Mayor == None) and (Menor == None):
                    i+= 1
                    j+= 1
                    PMax= [i, j]
                    i-= 1
                    j-= 1
                    Mayor= M[i][j]
                    Menor= M[i][j]
                else:
                    if M[i][j] > Mayor:
                        i+= 1
                        j+= 1
                        PMax= [i, j]
                        i-= 1
                        j-= 1
                        Mayor= M[i][j]
                    if M[i][j] <= Menor:
                        i+= 1
                        j+= 1
                        PMin= [i, j]
                        i-= 1
                        j-= 1
                        Menor= M[i][j]
        print("La posicion del elemento mayor se encruentra en: (fila {} - columna {}).".format(PMax[0], PMax[1]))
        print("La posicion del elemento menor se encruentra en: (fila {} - columna {}).".format(PMin[0], PMin[1]))  
        
    def Ejer37(matriz):
        matriz=[35,6,4], [3,5,6,4]
        vector = [0,0,0,0,0,0 ,0,0]   
        for p in range(3):
            vector[p] = matriz[0][p]
        for p in range(3,8):
            vector[p]= matriz[1][p-3]
        for i in range(8):
            for j in range(8-1):
                if vector[j]> vector[j+1]:
                    vector[j], vector[j+1] = vector[j+1], vector[j]
        print(vector)
    
    def Ejer43(self):
        miCadenaDeTexto = str("oso")
        if miCadenaDeTexto == miCadenaDeTexto[::-1]:
            print("Es palindroma")
        else:
            print("No es palindroma")

pres=Ejercicios()
#pres.Ejer1()
#pres.Ejer4()
#pres.Ejer7()
#pres.Ejer10()
#pres.Ejer13()
#pres.Ejer16()
#pres.Ejer19()
#pres.Ejer22()
#pres.Ejer25()
#pres.Ejer28()
#pres.Ejer31()
pres.Ejer41()
#pres.Ejer37()
#pres.Ejer40()
#pres.Ejer43()

