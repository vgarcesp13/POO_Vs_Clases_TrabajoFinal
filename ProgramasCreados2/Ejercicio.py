class Ejercicio:

    def Ejer1(self, N):
        n= int(N)
        if n%2 == 0:
            return("El numero ({}), es un numero par.".format(n))
        else:
            return("El numero ({}), no es un numero par.".format(n))
    
    def Ejer2(self, N1, N2):
        n1, n2= int(N1), int(N2)
        Pro= n1*n2
        return("{}x{}={}".format(n1, n2, Pro))

    def Ejer3(self, N1, N2):
        n1, n2= int(N1), int(N2)
        if n1 > n2:
            return("El numero {} es mayor que el numero {}.".format(n1, n2))
        elif N1 < N2:
            return("El numero {} es mayor que el numero {}.".format(n2, n1))
        else:
            return("El numero {} y el numero {}, son iguales.".format(n1, n2))
    
    def Ejer4(self, N1, N2):
        n1=int(N1)
        x= N2.split(',')
        n2= int(x[0])
        n3= int(x[1])
        if (n1>n2 and n1>n3):
            return("El numero: {}, es mayor".format(n1))
        elif (n2>n1 and n2>n3):
            return("El numero: {}, es mayor".format(n2))     
        elif (n3>n1 and n3>n2):
            return("El numero: {}, es mayor".format(n3))
        else:
            return("Los numeros son iguales.")
        
    def Ejer5(self,N):
        n= int(N)
        cont=0
        Lista= []
        while (cont <= 12):
            resp = n * cont
            Lista+= [("{}*{}={}".format(n,cont,resp))]
            cont+= 1
        return(Lista)

    def Ejer6(self, N):
        L= N.split(",")
        Cont= 0
        Acum1= 0
        Acum2= 1
        while Cont < 5:
            Acum1+= int(L[Cont])
            Acum2*= int(L[Cont])
            Cont+= 1
        return("La suma de la secuencia de numeros que ingreso es de: {}.\nEl producto de la secuencia de numeros que ingreso es de: {}.".format(Acum1, Acum2))
        
    def Ejer7(self, N):
        L= N.split(',')
        Cont= 0
        Acu= 0
        while Cont != -1:
            n=int(L[Cont])
            if n < 0:
                Cont= -1
            else: 
                Acu+=n
                Cont+=1
        return(Acu)

    def Ejer8(self,N1,N2):
        n1, n2, Cont, Acum= int(N1), int(N2), 0, 0
        while (Cont < n2):
            Acum+= n1
            Cont+= 1
        return(Acum)

    def Ejer9(self, N1, N2):
        n1, n2, Cont, L1, L2= int(N1), int(N2), 0, [], []
        while n1 >= 0:
            n1-= n2
            L1+=[n1]
            Cont+=1
            L2+= [Cont]
        return("(Cociente: {} - Residuo: {})".format(L2[-2], L1[-2]))
    
    def Ejer10(self, N):
        L= N.split(',')
        Cont= 0
        Acu= 1
        while Cont != -1:
            if L[Cont] != 'F':
                n=int(L[Cont])
                Acu*=n
                Cont+=1
            else:
                Cont= -1
        return(Acu)
    
    def Ejer11(self, N):
        L= N.split(',')
        Mayor= None
        for i in L:
            if Mayor == None:
                Mayor= int(i)
            else:
                if int(i) > Mayor:
                    Mayor=int(i)
        return("El numero mayor es: {}.".format(Mayor))

    def Ejer12(self, n):
        N= int(n)
        Aux= N
        A= ""
        while N > 0:
            R= N%2
            N=int(N/2)
            R=str(R)
            A+= R
            R= int(R)
        S= ""
        Cont= 0
        I= -1
        for i in A:
            Cont+= 1
        while Cont > 0:
            S+= A[I]
            Cont-= 1
            I-= 1
        return("El numero {} transformado en binario es: {}.".format(Aux, S))
    
    def Ejer13(self, N):
        Desde= int(N)
        acum= 0
        lista=[]
        while Desde < 30:
            if Desde%5 == 0:
                acum+=Desde
            lista+=[Desde]
            Desde+=3
        return("Numeros generados: {}.\nSuma de los multiplos de 5: {}.".format(lista, acum))

    def Ejer14(self, N):
        L= N.split(",")
        Cont= 0
        Acum= 0
        for i in L:
            I= int(i)
            Acum+= I
            Cont+= 1
        Prom= Acum/Cont
        return("El promedio es: ({}).".format(Prom))
    
    def Ejer15(self, N):
        L= N.split(",")
        Cont=0
        Mayor= None
        Menor= None
        while int(L[Cont])%2 == 0:
            if Mayor == None and Menor == None:
                Mayor= int(L[Cont])
                Menor= int(L[Cont])
            else:
                if int(L[Cont]) > Mayor:
                    Mayor= int(L[Cont])
                if int(L[Cont]) < Menor:
                    Menor= int(L[Cont])
            Cont+= 1
        return("El numero ayor es: ({}).\nEl numero menor es: ({}).".format(Mayor, Menor))
    
    def Ejer16(self, N):
        L= N.split(',')
        Acum= 0
        for i in L:
            if int(i)%2 ==0:
                Acum+=int(i)
        return("La suma de los numeros pares es: ({}).".format(Acum))

    def Ejer17(self, N):
        L= N.split(',')
        Acum= 0
        for i in range(len(L)):
            if i%2 == 0:
                Acum+= int(L[i])
        return("La suma de los numeros de las posiones pares es: ({}).".format(Acum))

    def Ejer18(self, N):
        n= int(N)
        Aux= n
        Acum= 1
        while n>=1:
            Acum*= n
            n-= 1
        return("El factorial del numero ({}) es: ({}).".format(Aux, Acum))

    def Ejer19(self, N):
        n= int(N)
        Aux= n
        Acum= 0
        while Aux >= 1:
            if n%Aux ==0:
                Acum+= 1
            Aux-= 1
        if Acum > 2:
            return("El numero ({}) no es un numero primo.".format(n))
        else:
            return("El numero ({}) es un numero primo.".format(n))
    
    def Ejer20(self, N):
        L= N.split(",")
        Acum=0 
        for i in L:
            Aux= int(i)
            Acum2= 0
            while Aux >= 1:
                if int(i)%Aux == 0:
                    Acum2+= 1
                Aux-= 1
            if Acum2 <= 2:
                Acum+= int(i)
        return("La suma de los numeros primos es de: ({}).".format(Acum))
    
    def Ejer21(self, N):
        L= N.split(",")
        Acum= 0
        for i in L:
            n= int(i)
            if n >= 1:
                Acu= 1
                while n > 1:
                    Acu*= n
                    n-= 1
                Acum+= Acu
        return("La suma de los factoriales es de: ({}).".format(Acum))

    def Ejer22(self, X):
        L= X.split(',')
        Acum1=0
        Acum2=1
        for i in L:
            n= int(i)
            if n%2 == 0:
                Acum1+= n
        for I in L:
            N= int(I)
            if N%5 == 0:
                Acum2*= N
        return('Suma de los numeros pares: ({}).\nProducto de los multiplos de 5: ({}).'.format(Acum1, Acum2))

    def Ejer23(self, X):
        L= X.split(',')
        L1= []
        for i in L:
            n= int(i)
            if n%2 == 0:
                L1+= [n]
        Mayor= None
        for I in L1:
            if Mayor == None:
                Mayor= I
            else:
                if I > Mayor:
                    Mayor= I
        return("El mayor numero par es: ({}).".format(Mayor))

    def Ejer24(self, X):
        L= X.split(',')
        L1= []
        L2= []
        for i in L:
            if int(i)%3 == 0:
                L1+= [int(i)]
        for I in L:
            if int(I)%5 == 0:
                L2+= [int(I)]
        Mayor= None
        for x in L2:
            if Mayor == None:
                Mayor= x
            else:
                if x > Mayor:
                    Mayor= x
        Menor= None
        for y in L1:
            if Menor == None:
                Menor= y
            else:
                if y < Menor:
                    Menor= y
        return("El mayor de los multiplos de 5 es: ({}).\nEl menor de los multiplos de 3 es: ({}).".format(Mayor, Menor))

    def Ejer25(self, X):
        V= X.split(",")
        Mayor= None
        P= 0
        for i in range(len(V)):
            n= int(V[i])
            if Mayor == None:
                Mayor= n
                P= i
            else:
                if n > Mayor:
                    Mayor= n
                    P= i
        return("El numero mayor se encuentra en a posicion: ({}).".format(P))

    def Ejer26(self, N, N1):
        A= N.split(',')
        B= N1.split(',')
        C= []
        for i in range(len(A)):
            C+= [int(A[i])+int(B[i])]
        return("La suma de los vectores es:\n{}.".format(C))
    
    def Ejer27(self, N, N1):
        A= N.split(',')
        B= N1.split(',')
        C= []
        for i in range(len(A)):
            C+= [int(A[i])+int(B[i])]
        Mayor= None
        for i in C:
            if Mayor == None:
                Mayor= i
            else:
                if i > Mayor:
                    Mayor= i
        return("El numero mayor del vector C es: ({}).".format(Mayor))
    
    def Ejer28(self, N):
        L= N.split(",")
        V= []
        for i in L:
            V+= [int(i)]
        for Recorrido in range(1, len(V)):
            for Posicion in range(len(V) - Recorrido):
                if V[Posicion] > V[Posicion + 1]:
                    Aux= V[Posicion]
                    V[Posicion]= V[Posicion+1]
                    V[Posicion + 1]= Aux
        return(V)
    
    def Ejer29(self, N, N1):
        V= N.split(',')
        n= int(N1)
        Cont= 0
        for i in V:
            if int(i) == n:
                Cont+= 1
        if Cont > 0:
            return("El numero ({}), si se encuentra en el vector.".format(n))
        else:
            return("El numero ({}), no se encuentra en el vector.".format(n))
    
    def Ejer30(self, N):
        L= N.split(",")
        V= [] 
        for i in L:
            n= int(i)
            if n > 1:
                Acum= 1
                while n >= 1:
                    Acum*= n
                    n-= 1
                V+= [Acum]
            else:
                V+= [n]
        return("El vector de lo factoriales es:\n({})".format(V))

    def Ejer31(self, N):
        V= N.split(',')
        L=[]
        for i in V:
            L+= [int(i)]
        for Recorrido in range(1, len(L)):
            for Posicion in range(len(L)-Recorrido):
                if L[Posicion] > L[Posicion+1]:
                    Aux= L[Posicion]
                    L[Posicion]= L[Posicion+1]
                    L[Posicion+1]= Aux
        return(L)
    
    def Ejer32(self, N, N1):
        n, n1, L= list(N), list(N1), []
        for i in range(len(n)):
            for j in range(len(n[i])):
                L[i][j]+= [int(n[i][j])+int(n1[i][j])]
        return(L)

    def Ejer33(self, N):

        pass

    def Ejer34(self, N):

        pass

    def Ejer35(self, N):

        pass

    def Ejer36(self, N):
        V= N.split(',')
        Acum= 0
        Mayor= None
        for i in range(len(V)):
            n= int(V[i])
            if i%2 == 0:
                Acum+= n
            else:
                if Mayor == None:
                    Mayor= n
                else:
                    if n > Mayor:
                        Mayor= n
        return("La suma de las posisiones pares da como resultado: ({}).\nEl numero mayor de las posiciones impares es: ({}).".format(Acum, Mayor))

    def Ejer39(self, N):
        V= N.split(',')
        L= []
        for i in V:
            n= int(i)
            Aux= n
            Cont= 0
            while Aux >= 1:
                if n%Aux == 0:
                    Cont+=1
                Aux-= 1
            if Cont <= 2:
                L+= [n]
        return("Los numeros primos del vector son:\n{}".format(L))

    def Ejer40(self, N, N1):
        x= N.find(N1)
        if x == -1:
            return("La palabra ({}) no se encuentra en el texto.".format(N1))
        else:
            return("La palabra ({}) si se encuentra en el texto.".format(N1))

    def Ejer41(self, N):
        L= N.split(' ')
        x= len(L)
        return("El texto contiene un total de ({}) palabras.".format(x))

    def Ejer42(self, N):
        L= N.split(' ')
        Mayor= None
        for i in L:
            if Mayor == None:
                Mayor= i
            else:
                if len(i) > len(Mayor):
                    Mayor= i
        return("La palabra de mayor longitud en el texto es: ({}).".format(Mayor))

    def Ejer43(self, N):
        if N == N[::-1]:
            return("Si es un palindromo.")
        else:
            return("No es un palindromo")

"""     def subincad(self, N, N1):
        n= N.split(' ')
        n.insert(len(n), N1)
        x= ' '.join(n)
        return(x) """