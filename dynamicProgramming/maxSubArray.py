"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

:type nums: List[int]
:rtype: int
"""
def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] = nums[i] + nums[i-1]
    return max(nums)

assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6, "Largest sum is 6"
assert maxSubArray([1]) == 1, "Largest sum is 1"
assert maxSubArray([-5,6,3,2,-9,3]) == 11, "Largest sum is 11"