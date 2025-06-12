'''
Datos:

Enter Principal: 5000
Enter Rate (%): 5
Enter Time (years): 2
Enter Compounds/year: 1

Resultados:
Total Amount: 5512.50
Compound Interest: 512.50
'''

# Programa en python para calcular el interés compuesto

def compound_interest1(principal, rate, time, n):
    # Convert annual rate percentage to decimal
    rate = rate / 100  
    # Apply compntound ierest formula
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return amount, interest

# Taking user inputs
P = float(input("Enter Principal: "))
R = float(input("Enter Rate (%): "))
T = int(input("Enter Time (years): "))
n = int(input("Enter Compounds/year: "))

# Calculating interest
total, interest = compound_interest1(P, R, T, n)

# Displaying results
print(f"Total Amount: {total:.2f}")
print(f"Compound Interest: {interest:.2f}")