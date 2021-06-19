class Articulo:
    def __init__(self,nom_art,cod,prec, mar,monto=0,tipo="Viveres"): #tipo = "Viveres" eso es el parámetro especial
        self.nombre_art = nom_art
        self.codigo = cod
        self.precio = prec
    
        self.marca = mar
        self.monto = monto
        self.tipo = tipo

    def monto_dsc(self):
        if(self.precio>100):
           self.monto= self.precio-(self.precio*0.20)
        elif (self.precio <= 100 and self.precio >=50):
           self.monto= self.precio-(self.precio*0.1)
        else:
           print(" Su valor a pagar es: {}".format(self.precio))
        print(" Su valor a pagar con el descuento es: {}".format(self.monto))
    def mostar_Art(self):
        print(" Producto: {},Codigo del producto: {}, Precio :{}, Marca_Del_Prod: {}, Tipo: {}".format(self.nombre_art, self.codigo, self.precio, self.marca, self.tipo))

articulo1=Articulo("Canasto_de_Viveres", "0024" ,200, "Conejo")
articulo1.mostar_Art()
articulo1.monto_dsc()
articulo2=Articulo("Pacas_De_Yogurt", "1310",30, "Toni", "Lacteos")
articulo2.mostar_Art()
articulo2.monto_dsc()

"""articulo2=Articulo("yogurt", "003", "lacteos", "3,50")
articulo2.monto_dsc()
articulo2.mostrar_Art()
articulo3=Articulo("labial", "006", "cosmeticos", "4,00")
articulo3.monto_dsc()
articulo3.mostrar_Art()
articulo4=Articulo("Carlos", "0710701566", '13', "Yaguachi", "Colegio")
articulo4.monto_dsc()
articulo4.mostrar_Art()"""