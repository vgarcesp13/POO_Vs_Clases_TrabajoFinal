from marca import Marca
from grupo import Grupo
class Producto:
    def __init__(self,codigo,des,pre,sto,mar,gru,est):
        self.id= codigo
        self.descripcion= des
        self.precio= pre
        self.stock= sto
        self.marca= mar
        self.grupo= gru
        self.estado= est
    def MostrarProducto(self):
        return ("{} - {} - {}".format(self.id,self.descripcion,
                                    self.precio,self.stock,self.marca.descripcion,
                                    self.grupo.descripcion,self.estado))
    grupo1 = Grupo(1, "Embutidos", True)
    grupo2 = Grupo(2, "LActeos", True)
    grupos = [grupo1,grupo2]
    marca1 = Marca(1, "Plumrose", True)
    marca2 = Marca(2, "Toni", True)
    marcas = [marca1,marca2]
    
    productos = []
    for i in range (1,5):
        nombre = input("Ingrese productos: ")
        precio = input*("ingrese un precio: ")
        stock = input("Ingrese un stock: ")
        producto=Producto(i,nombre,pre,sto,grupo1, marca1, True)
        producto.append(producto)