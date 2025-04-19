number = 456
    #   456  0
    #   57  1
    #   7   7
oct=0
mult=1
while number !=  0:
    rem=number%8
    print(rem)
    oct= oct + (rem*mult)
    mult*=10
    number//=8
print(oct)