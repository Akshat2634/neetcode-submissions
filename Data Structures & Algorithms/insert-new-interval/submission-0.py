class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key=lambda x:x[0])

        ans = []
        ans.append(intervals[0])

        for i in range(1,len(intervals)):
            curr = intervals[i]
            prev = ans[-1]

            if curr[0]<=prev[1]:
                prev[1]= max(prev[1],curr[1])
            else:
                ans.append(curr)

        return ans
        