"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        starts = sorted(i.start for i in intervals)
        print(starts)
        ends   = sorted(i.end   for i in intervals)
        print(ends)
        
        rooms = 0
        max_rooms = 0
        s = e = 0
        
        while s < len(starts):
            if starts[s] < ends[e]:        # a meeting starts before any current ends
                rooms += 1
                s += 1
            else:                           # a meeting ends before/at the next start
                rooms -= 1
                e += 1
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms