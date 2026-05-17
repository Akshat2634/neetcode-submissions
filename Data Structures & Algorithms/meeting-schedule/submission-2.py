
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        intervals.sort(key = lambda x:x.start)
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            prev = ans[-1]
            curr = intervals[i]

            if curr.start<prev.end:
                return False
            ans.append(curr)

        return True

        

