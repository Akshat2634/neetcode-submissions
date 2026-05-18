class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        ans = []
        ans.append(intervals[0])

        for i in range(1,len(intervals)):
            curr = intervals[i]
            prev = ans[-1]

            if curr[0]<=prev[1]:
                prev[1] = max(curr[1],prev[1])
            else:
                ans.append(curr)


        return ans
        