

'''A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

'''

def count_good_numbers(n):
    if n==0:
        return 0
    
    mod=10**9+7

    even_index=(n+1)//2
    odd_index=n//2

    def powermode(base,exponent,mod):

        result=1

        while exponent>0:
            if exponent%2==1:
                result=(result*base)%mod

            base=(base*base)%mod

            exponent=exponent//2
        
        return result
    
    
    even_power=powermode(5,even_index,mod)
    odd_power=powermode(4,odd_index,mod)

    return (even_power*odd_power)%mod

print(count_good_numbers(4))
print(count_good_numbers(7))
print(count_good_numbers(100000))

print(count_good_numbers(0))

