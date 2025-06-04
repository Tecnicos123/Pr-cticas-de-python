class operaciones(): 
    def __init__(self):
        self.n1 = int(input("el primer numero es: "))
        self.n2 = int(input("el segundo numero: "))
    
    def suma(self):
        print("el resultado de la suma es: ",self.n1 + self.n2)
    
    def resta(self):
        print("el resultado de la resta es: ",self.n1 - self.n2)
    
    def multiplicacion(self):
        print("el resultado de la multiplicacion es: ",self.n1 * self.n2)
    
    def division(self): 
        print("el resultado de la division es: ", self.n1 / self.n2)
    
def main():
    op = operaciones()
    op.suma()
    op.resta()
    op.multiplicacion()
    op.division()
main()