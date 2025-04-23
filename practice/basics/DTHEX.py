number = 458
    #   458  A
    #   28  C
    #   1   1
    #  1CA

hex=""
while number !=  0:
    rem=str(number%16)
    if(rem=='10'):
        rem='A'
    elif(rem=='11'):
        rem='B'
    elif(rem=='12'):
        rem='C'
    elif(rem=='13'):
        rem='D'
    elif(rem=='14'):
        rem='E'
    elif(rem=='15'):
        rem='F'
    print(rem)
    hex+=rem
    number//=16
print(hex)