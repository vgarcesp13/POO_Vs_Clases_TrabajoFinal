class Articulo :
    def __init__(self, nom, codigo, precio, marca, tipo= "viveres"):
        self.nombre = nom
        self.codigo = codigo
        self.precio = precio
        self.marca = marca
        self.tipo = tipo
        
    def IVA (self,IVA ):
        return self.precio*IVA
    
    def MostrarIVA(self):
        valor= self.IVA(0.12)
        tot_prod= self.precio+ valor
        print(" Nombre del producto: {}, Cod.prod:  {}, Precio: {}, Marca:  {}, Tipo:  {}".format(self.nombre, self.codigo, self.precio, tot_prod, self.tipo) )

art1 = Articulo("arroz", "001", 0.44, "Conejo")
art1.MostrarIVA()
art2 = Articulo("labial", "002", 4.46, "AVON", "Cosmetico")
art2.MostrarIVA()
