def findMax(nums):
    maxValue = nums[0]
    for num in nums:
        if num > maxValue:
            maxValue = num
    return maxValue
