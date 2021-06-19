class Marca:
    def __init__(self,id,des,est):
        self.id= id
        self.descripcion= des
        self.estado= est    

    def MostrarMarca(self):
        return ("{} - {} -   {}".format(self.id,self.descripcion,self.estado))

marca1= Marca('1', 'Plumrose',True )
marca2= Marca('2', 'Iberica',True )
resp = marca1.MostrarMarca()

print("Id  Descripción  Estado")
print(resp)
print(marca2.MostrarMarca())
marcas = []
for i in range(1,5):
    nombre = input("Ingrese marca: ")
    marca = Marca(i, nombre, True)
    marcas.append(marca)

for marca in marcas:
    print(marca.MostrarMarca())