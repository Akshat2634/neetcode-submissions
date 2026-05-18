class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        ans = []
        ans.append(intervals[0])
        cnt = 0

        for i in range(1,len(intervals)):
            prev = ans[-1]
            curr = intervals[i]

            if curr[0]<prev[1]:
                cnt+=1
            else:
                ans.append(curr)

        return cnt
        