# 724. Find pivot index

# Учитывая массив целых чисел nums, вычислите pivot index этого массива.
# Pivot index - это индекс, в котором сумма всех чисел, 
# расположенных строго слева от индекса, равна сумме всех чисел, 
# расположенных строго справа от индекса.

# Если индекс находится на левом краю массива, то левая сумма равна 0,
# потому что слева нет элементов. Это также относится к правому краю массива.
# Верните самый левый сводный индекс. Если такого индекса не существует, верните -1.

'''
Input: nums = [1,7,3,6,5,6]
Output: 3
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        allSum = 0
        for num in nums:
            allSum += num

        # allSum - i - pxSum = pxSum
        pxSum = 0
        for i, num in enumerate(nums):
            
            if allSum - num - pxSum == pxSum:
                return i
            
            pxSum += num

        return -1