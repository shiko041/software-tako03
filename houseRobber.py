from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        sum1=0
        sum2=0
        for i in range(0, len(nums),2):
            sum1+=nums[i]
        for i in range(1, len(nums),2):
            sum2+=nums[i]
        if sum1>sum2:
            return sum1
        else:
            return sum2
solution = Solution()
print(solution.rob([2, 3, 2]))  
print(solution.rob([1, 2, 3, 1]))
