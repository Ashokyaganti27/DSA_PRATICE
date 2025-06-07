"""Given a sorted array of nums and an integer x, write a program to find the upper bound of x. 
The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than a given key i.e. x.
If no such index is found, return the size of the array.
"""
def upperBound( nums, x):

    start=0
    end=len(nums)-1
    ans=len(nums)
    while start<=end:
        m=(start+end)//2
        if nums[m]>x:
            ans=m
            end=m-1
        else:
            start=m+1
    return ans

ans=upperBound([4,5,6,6,6,9,10],6)
print(ans)