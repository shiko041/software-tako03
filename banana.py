import math
class Solution:
    def minEatingSpeed(self, piles, h):
        def time_needed(piles, k):
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)
            return hours_needed

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if time_needed(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1

        return left
solution = Solution()
p = [3, 6, 7, 11]
print(solution.minEatingSpeed(p, 8))
print("------")
p = [30, 11, 23, 4, 20]
print(solution.minEatingSpeed(p, 5))
print("------")
print(solution.minEatingSpeed(p, 6))
