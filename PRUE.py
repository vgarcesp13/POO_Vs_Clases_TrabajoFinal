class Eje:
    def fibonacci(self,serie):
            primero,segundo,siguiente,c=0,1,1,2
            lista = [primero,segundo]
            while c < serie:
                lista.append(siguiente)
                primero=segundo
                segundo=siguiente
                siguiente = primero+segundo
                c=c+1
            return lista
e=Eje()
e.fibonacci(3)
