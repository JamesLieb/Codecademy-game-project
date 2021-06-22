class User:
    user=input()
    def __repr__(self):
        print("Hello, please insert the principal amount of your loan, the interest rate and the total number of monthly payments, in the following format (1,2,3)")






class Calculator(User):
    def __init__(self):
        self.P=user[0]
        self.r=user[1]
        self.N=[user[2]]
    def calculate(self):
        try:
            monthly_payment=((self.r)*(self.P))/(1-(1+self.r)**(-self.N))
        except:
            ValueError
            print("Only use numbers for the input, and make sure to seperate the values by a comma")

        return round(monthly_payment,2)
    
example=Calculator()
print(example.calculate((200000,6,300)))
    
    