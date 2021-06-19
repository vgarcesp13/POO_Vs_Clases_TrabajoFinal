class operacion:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2
    def suma(self):
        return self.numero1+self.numero2
    def resta(self):
        return self.numero1-self.numero2
    def multiplicacion(self):
        return self.numero1*self.numero2
    def division(self):
        return self.numero1/self.numero2
    def division_entera(self):
        return self.numero1//self.numero2
    def residuo(self):
        return self.numero1%self.numero2
    def exponente(self):
        return self.numero1**self.numero2
    def mostrar_datos(self):
        print("La suma de: {}+{} es:{}".format(self.numero1,self.numero2,self.suma()))
        print("La resta de: {}-{} es:{}".format(self.numero1,self.numero2,self.resta()))
        print("La multiplicacion de: {}*{} es:{}".format(self.numero1,self.numero2,self.multiplicacion()))
        print("La division de: {}/{} es:{}".format(self.numero1,self.numero2,self.division()))
        print("La divisionEntera de: {}//{} es:{}".format(self.numero1,self.numero2,self.division_entera()))
        print("El residuo de: {}%{} es:{}".format(self.numero1,self.numero2,self.residuo()))
        print("El exponente de: {}**{} es:{}".format(self.numero1,self.numero2,self.exponente()))
ope= operacion(2,4)
ope.mostrar_datos()