<<<<<<< HEAD
class Calculator():
    def __init__(self,P,r,N):
        self.P=P
        self.r=r
        self.N=N
    def __repr__(self):
        print("Hello, please insert the principal amount of your loan, your given interest rate and the total number of monthly payments to be made.")
    def calculate(self):
        try:
            monthly_payment=((self.r)*(self.P))/(1-(1+self.r)**(-self.N))
        except:
            ValueError
            print("Only use numbers for the input, and make sure to seperate the values by a comma")
            
        return round(monthly_payment,2)
    
    
    
=======

>>>>>>> 7c1e60f49e8ff53a70763c7a3207c69860a7378a
