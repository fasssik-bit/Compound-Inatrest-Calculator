# Compound Interest Calculator
Principal=0
Rate=0
Time=0
while True :
    Principal = float(input("enter your Principal number :"))
    if Principal > 0:
        break
        print("enter number is invalid")

while  True:
    Rate = float(input("enter your rate :"))
    if Rate > 0:
        break
        print("your enter number is invalid")

while  True :
    Time = int(input("enter your Time :"))
    if Time > 0:
        break
        print("your inout is invalid")

Total = Principal *pow((1+Rate/100),Time)
print((f"Balnce after {Time} year/s {Total:.2F}"))
