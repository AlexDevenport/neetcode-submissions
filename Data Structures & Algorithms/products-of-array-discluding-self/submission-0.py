# Учитывая целочисленный массив nums, верните массив output,
# где output[i] является произведением всех элементов nums,
# кроме nums[i].

# Каждое произведение гарантированно соответствует 32-разрядному
# целому числу.

# Follow-up: Не могли бы вы решить это в 
# O(n) времени без использования операции деления?

# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        result = [1] * length # префиксное произведение

        # Произведение слева от i (префикс)
        left = 1
        for i in range(length):
            result[i] = left
            left *= nums[i]
        
        # Произведение справа от i (суффикс)
        right = 1
        for i in range(length-1, -1, -1):
            result[i] *= right
            right *= nums[i]
        
        return result