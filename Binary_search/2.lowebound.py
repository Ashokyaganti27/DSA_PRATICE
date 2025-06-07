"""Given a sorted array of nums and an integer x, write a program to find the lower bound of x. 
The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
If no such index is found, return the size of the array.
"""
def lowerBound(nums, x):
    
    start=0
    end=len(nums)-1
    ans=0
    while start<=end:
        middle=(start+end)//2
        if nums[middle]>=x:
            ans=middle
            end=middle-1
        else:
            start=middle+1
    return ans

ans=lowerBound([1,3,3,4,4,4,6,7,8],3)
print(ans)

















