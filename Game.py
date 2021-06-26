
print("Hello, please insert your principal mortgage amount, your interest rate on the mortgage, followed by the total number of payments in the following format 1,2,3")
a=input()
l=a.split(',')
P=float(l[0])
r=float(l[1])
N=float(l[2])
r=(r/100)/12
monthly_payment=round((r*P)/(1-(1+r)**(-N)),2)
total_interest=round(monthly_payment*N-P,2)
print("Your expected monthly payment is ${monthly} and your expected interest paid is ${interest}.".format(monthly=monthly_payment,interest=total_interest))


    
    