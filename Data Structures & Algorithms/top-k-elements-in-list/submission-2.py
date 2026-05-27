# Given an integer array nums and an integer k, 
# return the k most frequent elements within the array.

# The test cases are generated such that the answer 
# is always unique.

# You may return the output in any order.

# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        for num in nums:
            if num not in count.keys():
                count[num] = 1
            else:
                count[num] += 1

        # сортируем словарь по значениям по убыванию
        count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

        for i in range(k):
            ans.append(list(count.keys())[i])

        return ans