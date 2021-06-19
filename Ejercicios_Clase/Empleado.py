class Empleado:
    def __init__(self,nom,ced,sue,car,dep="RRHHS"): #parametro opcional tiene por default 
        self.nombre = nom
        self.cedula = ced
        self.sueldo = sue
        self.cargo = car
        self.departamento = dep
    
    def horas(self,horas):
        return self.sueldo/30/8*horas
    
    def mostrarNomina(self): 
        vhoras = self.horas(10) #llama a las horas, trabaja 10 horas
        toting = self.sueldo+vhoras #son propia s de la funcion no de la clase total de ingressos
        print("{} {} {} {} {}".format(self.nombre,self.cedula,self.sueldo,vhoras,toting))
        
emp1 = Empleado("Dani", "0986958878", 1000, "Analista", "Bodega")
emp1.mostrarNomina() #llama al metodo horas con 10, y retorna el valor hora del empleado
        #llavces.format es 
emp2 = Empleado("Juan", "0999986789", 1200, "Jefe", "Area")
emp2.mostrarNomina()