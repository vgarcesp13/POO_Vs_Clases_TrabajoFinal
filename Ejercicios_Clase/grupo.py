class Grupo:
    def __init__(self,id,des,est):
        self.id= id
        self.descripcion= des
        self.estado= est    

    def MostrarGrupo(self):
        return ("{} - {} -   {}".format(self.id,self.descripcion,self.estado))

grupos = []
for i in range(1,5):
    nombre = input("Ingrese grupo: ")
    grupo = Grupo(i, nombre, True)
    grupos.append(grupo)
print("Id  Descripción  Estado")
for grupo in grupos:
    print(grupo.MostrarGrupo())