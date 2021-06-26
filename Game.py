






class Calculator():
    def __init__(self,P,r,N):
        self.P=P
        self.r=r
        self.N=N
    def calculate(self):
        self.r=(self.r/100)/12
        try:
            monthly_payment=((self.r)*(self.P))/(1-(1+self.r)**(-self.N))
            return round(monthly_payment,2)
        except:
            ValueError
            print("Only use numbers for the input, and make sure to seperate the values by a comma")
            return

        
    
example=Calculator(200000 ,6.5,360)
print(example.calculate())
    
    