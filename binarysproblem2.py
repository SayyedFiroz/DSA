# given a sorted list find how manny time it rotated;rotation means moving  last element to the first in list

# brute force output by my own
nums = [25, 29, 30,40,5, 6, 7, 9, 11]


"""def count_rotation(nums):
    rotate = 0
    min_range = 0
    min = nums[0]
    max = nums[0]
    for i in range(0, len(nums)):
        if nums[i] < min:
            min = nums[i]
    for i in range(0, len(nums)):
        if nums[i] > max:
            max = nums[i]

    for i in range(0, len(nums)):
        if nums[i] == min:
            min_range = i

    for i in range(0, min_range):
        if nums[i] > min:
            rotate += 1
"""

# linear search by instructor:
def linear_rotate(nums):
    rotate=0
    for i in range(0,len(nums)-1):
        if i>0 and nums[i] < nums[i-1]:
            rotate+=1
    return rotate

linear_rotate(nums)

#binary search
def binary_rotate(nums):
    lo=0
    hi=len(nums)-1
    while lo<=hi:
        mid=(lo+hi)//2
        mid_number=nums[mid]
        if mid > 0 and nums[mid-1]>mid_number:
            return mid
        elif mid_number < nums[hi]:
            hi=mid-1
        else:
            lo=mid+1
    return -1

result=binary_rotate(nums)
print(result)


# test cases
test = {'input': {'nums': [19, 25, 29, 5, 6, 7, 9, 11, 14]}, 'output': 3}
test1={'input': {'nums': [1,2,3,4,5,6]}, 'output': 0}
test2={'input': {'nums': [16, 5, 6, 7, 9, 11, 14]}, 'output': 1}
