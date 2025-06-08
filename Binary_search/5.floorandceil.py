"""Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. 
The floor of x is the largest element in the array which is smaller than or equal to x. 
The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.
"""
def getfloorceil(li,l):
    start=0
    end=len(li)-1
    floor = -1
    ceil= -1
    while start<=end:
        m=(start+end)//2
        if li[m]==l:
            floor =m
            ceil =m
            return floor , ceil
        elif li[m]<l:
            floor=m
            start=m+1
        else:
            ceil=m
            end=m-1
    return floor , ceil

print(getfloorceil([3,4,5,7,8,19],19))