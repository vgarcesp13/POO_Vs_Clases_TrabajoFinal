"""class Estudiante:
    def __init__(self,nom,carr,conct,ed,nc= 'Ecuatoriana'):
        self.nombre=nom
        self.carrera=carr
        self.conctacto=conct
        self.edad=ed
        self.nacionalidad=nc
    def may_men(self):
        if self.edad >=18:
            print("Es mayor de edad")
        elif self.edad <18 and self.edad>=1:
            print("Es menor de edad")
        else:
            print("Edad ingresa no es valida")
    def presentar(self):
        print("{},{},{},{}, {}".format(self.nombre, self.carrera, self.conctacto, self.edad, self.nacionalidad))
estu1=Estudiante ("Hernan", "Software", "09878", 18)       
estu1.presentar()
estu1.may_men()
estu2=Estudiante ("Teresa", "Software", "0987898", -5)       
estu2.presentar()
estu2.may_men()"""

class Articulo:
    def __init__(self,nom,mar,mod,valor,cost,exis):
        self.nombre=nom
        self.marca=mar
        self.modelo=mod
        self.valor_pag=valor
        self.costo=cost
        self.existencia=exis
    def cal_valor_pagar(self):
        prod1=float(input("Ingrese valor del producto 1"))
        prod2=float(input("Ingrese valor del producto 2"))
        prod3=float(input("Ingrese valor del producto 3"))
        prod4=float(input("Ingrese valor del producto 4"))
        self.valor_pag= (prod1+prod2+prod3+prod4)
        IVA= self.valor_pag*1.12
        print("Subtotal: {}, \:Valor total a pagar: {}")
        return (IVA)
    def mostrarArticulo(self):
        print("{},{},{},{},{},{},{}".format(self.nombre,self.marca,self.modelo,self.valor,self.costo,self.existencia,utilidad))
print('Articulo Nº 1\n')
articulo1= ('Detergente','deja','en polvo',2,5,3)
articulo1.mostrarArticulo()
        print('calcular el valor a pagar de 2 detergentes: {} '.format(articulo1.calcularTotal(3) ))

    articulo2= ('Jabon','Protex','Liquido',4,3,1)
    print('\nArticulo Nº 2\n')
    articulo2.mostrarArticulo()
