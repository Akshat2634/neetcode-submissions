class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:x[1])

        ans = [intervals[0]]
        cnt = 0
        for i in range(1,len(intervals)):
            curr = intervals[i]
            prev = ans[-1]

            if curr[0]<prev[1]:
                cnt+=1
            else:
                ans.append(curr)

        return cnt
        