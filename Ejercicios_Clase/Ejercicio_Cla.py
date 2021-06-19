class Notas:
    #Constructor de la Clse en python con parámetros
    def __init__(self, est, asig, n1=30, n2=30, exam=40):
        self.estudiante = est
        self.asignatura = asig
        self.nota1 = n1
        self.nota2 = n2
        self.examen = exam

    def promedio(self):
        prom = (self.nota1 +self.nota2+self.examen)
        return prom  
    def mostrarDatos(self):
        pm = self.promedio() #va a ser igual a lo que retorne prom
        print("Estudiante: {}, Asignatura: {}, Nota final: {}".format(self.estudiante, self.asignatura, pm))
#Instance of the Class: Creation of objetcs
#Se llama al constructor cuando se instancia la clase
#Se instancia la clase cuando se crea una variable igual al nombre de la clase
est1= Notas("Freddy", "POO", 20,20,30 ) #Atributos que creo el constructor
est1.mostrarDatos()
'''est2= Notas("Ana", "Arquitectura" ) 
est2.examen=10
p=est2.promedio()
print(est2.nota1,est2.nota2,est2.examen,p)
est2.mostrarDatos()'''
        