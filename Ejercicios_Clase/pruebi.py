#ejercicio 20 Anthony
    def Ejer20 (self):
        i,cont, suma,n=0,2,0,0
        for i in range(4):
            num= int(input("Ingrese un numero: "))
        while (num %cont==0):
            cont= cont+1
            if cont==num:
             suma= suma+num
        print(suma)
    #ejercicio 11
    def Ejer10 (self):
        x,n,num,n_mayor= 1,0,0,0
        num=(int(input("Ingrese el total de numero a calcular: ")))
        while x<= num:
            n= int(input("Ingrese un numero: "))
            if x==1 and n %2==0:
                n_mayor= n
            elif n> n_mayor and n %2==0:
                n_mayor= n
            x= x+1
        print("El numero mayor es: ", n_mayor)