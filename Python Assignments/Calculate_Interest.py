K0 = float(input("Enter Initial balance (K0) "))
rate = float(input("Enter interest rate "))
n = int(input("Enter number of years "))

i = 0
while i < n:
    K0 *= 1 + rate / 100.0
    i += 1
    print(i, K0)
print("Capital after " + str(n) + " years: " + str(K0))
