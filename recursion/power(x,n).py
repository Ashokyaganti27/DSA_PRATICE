

"Implement pow(x, n), which calculates x raised to the power n (i.e., xn)."


def powermod(pow,exponent):

    result=1

    if exponent<0:
        exponent=abs(exponent)
        pow=1/pow

    while exponent>0:

        if exponent%2==1:

            result=result*pow
        
        pow=pow*pow
        
        exponent=exponent//2
    

    return result

# print(powermod(2.00000,-2))


# recursive version 
def powermodrecursive(x, n):
    if n == 0:
        return 1
    if n<0:
        return 1/powermodrecursive(x,-n)

    result = powermodrecursive(x, n // 2)

    if n % 2 == 0:
        return result * result
    else:
        return result * result * x

print(powermodrecursive(2,10))
print(powermodrecursive(2,-2))
print(powermodrecursive(210,10))


