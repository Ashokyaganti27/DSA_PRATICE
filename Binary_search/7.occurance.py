""" You are given a sorted array containing N integers and a number X,
 you have to find the occurrences of X in the given array.
"""

def OccuranceOfelement(nums,x):
    start,end=0,len(nums)-1
    small=len(nums)
    big=len(nums)
    while start<=end:
        mid=start+(end-start)//2
        if nums[mid]>=x:
            small=mid
            end=mid-1
        else:
            start=mid+1
    start,end=0,len(nums)-1
    while start<=end:
        mid=start+(end-start)//2
        if nums[mid]>x:
            big=mid
            end=mid-1
        else:
            start=mid+1 
            
    if small==len(nums) or nums[small]!=x :
        return "These element not present"
            
    return [big-small]

print(OccuranceOfelement([4,5,6,6,6,6,10],6))