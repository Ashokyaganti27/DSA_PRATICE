# binary search

def search(nums,target):
    start=0
    end=len(nums)-1
    while start<=end:
        middle=(start+end)//2
        if nums[middle]==target:
            return middle
        elif nums[middle]<target:
            start=middle+1
        else:
            end=middle-1
    else:
        return -1

ans=search([4,7,9,10,13,16],90)
print(ans)