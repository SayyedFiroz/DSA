def binary_Search(lo,hi,condition):
    while lo<=hi:
        mid=(lo+hi)//2
        result=condition(mid)
        if result=='found':
            return mid
        elif result=='left':
            hi=mid-1
        else:
            lo=mid+1
    return -1
def first_postition(nums,target):
    def condition(mid):
        if nums[mid]==target:
            if mid>0 and nums[mid-1]==target:
                return 'left'
            return 'found'
        elif nums[mid]<target:
            return 'right'
        else:
            return 'left'

    return binary_Search(0,len(nums)-1,condition)

def last_postition(nums,target):
    def condition(mid):
        if nums[mid]==target:
            if mid<len(nums)-1 and nums[mid+1]==target:
                return 'right'
            return 'found'
        elif nums[mid]<target:
            return 'right'
        else:
            return 'left'
    return binary_Search(0,len(nums)-1,condition)

def first_last(nums,target):
    return first_postition(nums,target), last_postition(nums,target)


class Solution:
    def searchRange(self, nums, target):
        return first_last(nums,target)

s1=Solution()
nums=[1,2,2,3]
target=2
result=s1.searchRange(nums,target)
print(result)