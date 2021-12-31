# https://leetcode-cn.com/problems/two-sum/
from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                index = nums.index(target - nums[i], i + 1 )
                if index > 0:
                    return [i, index]
            except ValueError:
                continue


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
