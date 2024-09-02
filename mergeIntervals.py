from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = []
        prevstart, prevend = intervals[0]
        for start, end in intervals[1:]:
            if start <= prevend:
                prevend = max(prevend, end)
            else:
                merged.append([prevstart, prevend])
                prevstart, prevend = start, end
        merged.append([prevstart, prevend])
        return merged

solution = Solution()
print(solution.merge([[2,6],[1,3],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]]))  # Output: [[1,5]]
