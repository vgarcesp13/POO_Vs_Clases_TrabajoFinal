class prueba:   

    def a(self):
     num = 123
     respuesta = [3,2,1]
     invertido = []
         while num > 0:
            invertido.append(num/10)
             num = num // 10
         return invertido

pres=prueba()
pres.a()