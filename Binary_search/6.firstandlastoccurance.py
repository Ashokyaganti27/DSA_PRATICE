"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1]
"""
def firstastoccurance(nums,x):

    if len(nums)==0:
        return [-1,-1]
    
    start,end=0,len(nums)-1
    first=-1
    while start<=end:
        mid=(start+end)//2
        
        if nums[mid]==x:
            first=mid
            end=end-1
        elif nums[mid]<x:
            start=mid+1
        else:
            end=mid-1
    start,end=0,len(nums)-1
    end=len(nums)-1
    last=-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==x:
            last=mid
            start=mid+1
        elif nums[mid]<x:
            start=mid+1
        else:
            end=mid-1
    return [first ,last]
    
print(firstastoccurance([3,6,9,10,12,12,12,67,90],12))
print(firstastoccurance([],0))