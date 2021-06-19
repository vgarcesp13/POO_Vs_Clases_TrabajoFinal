class Calculos():
    
    def fibo(self,serie):
        prime,segun,siguiente,c=0,1,1,2
        lista= [prime,segun]
        print(lista)
        while c < serie:
            print(siguiente)
            lista.append(siguiente)
            prime=segun
            segun=siguiente
            siguiente= prime+segun
            c=c+1
        return lista

    def primo(self,num):
        c,primo=2,True
        while c < num and primo == True:
            if num%c == 0: primo==False
            else: c= c+1
        return primo
    
    def divisores(self,num):
        return [divisor for divisor in range(1,num) if num%divisor==0]

    def invertirNumero(self,num):
        invertido=[]
        while num>0:
            invertido.append(num%10)
            num= num // 10
        return invertido
    
    def AcuDivisores(self,num):
        divisores = self.divisores(num)
        acu=0
        for divisor in divisores:
            acu=acu + divisor
        return acu
    
    def perfecto(self,num):
      return True if self.AcuDivisores(num)==num else False
  
    def amigos(self,num1,num2):
        return self.AcuDivisores(num1) == self.AcuDivisores(num2)
    
    def primoGemelos(self,num1,num2):
        return self.primo(num1)== self.primo(num2) and abs(num1-num2)==2
    
    def base2_10(self,num):
        digitos= self.invertirNumero(num)
        acu=0
        for exp,digito in enumerate(digitos):
            print(exp,digito)
            acu+= digito*2**exp
        return acu
    
    def base10_2(self, n):
        N= int(n)
        Aux= N
        A= ""
        while N > 0:
            R= N%2
            N=int(N/2)
            R=str(R)
            A+= R
            R= int(R)
        S= ""
        Cont= 0
        I= -1
        for i in A:
            Cont+= 1
        while Cont > 0:
            S+= A[I]
            Cont-= 1
            I-= 1
        return S
    
    def cualquierBase(self,nume,base):
        cadeConversion= "0123456789ABCDEF"
        if nume < base:
            return cadeConversion[nume]
        else:
            return self.cualquierBase(nume//base,base)+cadeConversion[nume%base]
        
        

        
                
# cal= Calculos()
# cal.perfecto(6)