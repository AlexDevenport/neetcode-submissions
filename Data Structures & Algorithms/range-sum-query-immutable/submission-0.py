# 303. Range sum query - Immutable

# Каждый элемент префиксного массика - сумма всех предыдущих элементов
# Вычислите сумму элементов чисел между индексами left и right включительно,
# где left <= right.


'''
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]
'''


from typing import List


class NumArray:
    # time: O(n)
    # mem:  O(n)
    def __init__(self, nums: List[int]) -> None:
        # делаем префиксный массив
        # [1, 2, 3] -> [0, 1, 3, 6]
        prefix_sum = [0, ]
        
        for i, num in enumerate(nums):
            prefix_sum.append(prefix_sum[-1] + num)

        self.prefix_sum = prefix_sum

    def sumRange(self, left: int, right: int) -> int:

        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)