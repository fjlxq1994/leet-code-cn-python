# https://leetcode-cn.com/problems/count-special-quadruplets/
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if nums[l] == nums[i] + nums[j] + nums[k]:
                            num += 1
        return num


input = [2, 16, 9, 27, 3, 39]
solution = Solution()
print(solution.countQuadruplets(input))
