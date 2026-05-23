class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)

        intervals.sort(key= lambda x:x[0])

        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            last = ans[-1] 
            curr = intervals[i]

            if curr[0]<=last[1]:
                last[1] = max(curr[1],last[1])

            else:
                ans.append(curr)

        return ans