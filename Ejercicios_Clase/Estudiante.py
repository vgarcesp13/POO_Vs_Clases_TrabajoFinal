class Estudiante:
    def __init__ (self, nomb, eda, ced,correo, totnot=0, secc= "Matutina"):
        self.nombre = nomb
        self.edad = eda
        self.cedula = ced
        self.email= correo
        self.totalNotas = totnot
        self.seccion = secc 
        
    def suma_notas(self): 
        
        print("Ingrese Las notas")
        n1= float (input ("Ingrese la Primera Nota: "))
        n2= float (input ("Ingrese la Segunda Nota: "))
        n3= float (input ("Ingrese la Tercera Nota: "))
        if ((n1 >=1 and n2>=1 and n3>=1) and (n1 <=15 and n2 <=15 and n3 <=15)):
            self.totalNotas= n1+n2+n3
        else:
            print("Alguna nota ingresada no es valida")
        promedioFinal = self.totalNotas/3
        print("El promedio final de {} es: {} ".format(self.totalNotas, promedioFinal))
    def MostrarDatos(self):
        print("{} {} {} {} {}".format(self.nombre,self.edad, self.cedula, self.email, self.seccion))
estudiante1 = Estudiante("Dilan", "15", "0941984106", "dilan_hernan@gmail.com" )
estudiante1.MostrarDatos()
estudiante1.suma_notas()
estudiante2 = Estudiante("Freddy", "18", "0997066291", "freddy-mas@hotmail.com", "Vespertina" )
estudiante2.MostrarDatos()
estudiante2.suma_notas()