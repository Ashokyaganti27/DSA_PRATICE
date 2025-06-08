"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the index where 
it would be if it were inserted in order."""

def searchInsert( nums, target):

    start=0
    end=len(nums)-1
    ans=len(nums)
    while start<=end:
        m=(start+end)//2
        if nums[m]>=target:
            ans=m
            end=m-1
        else:
            start=m+1
    return ans

print(searchInsert([3,7,8,9,12],13))