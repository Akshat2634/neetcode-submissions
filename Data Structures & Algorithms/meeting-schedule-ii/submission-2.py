"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_intervals = sorted(i.start for i in intervals)
        end_intervals = sorted(i.end for i in intervals)
        i = 0
        j = 0

        room = 0
        max_rooms = 0


        while i<len(start_intervals) and j<len(end_intervals):
            if start_intervals[i]<end_intervals[j]:
                room+=1
                i+=1
            else:
                room-=1
                j+=1
            max_rooms = max(room,max_rooms)

        return max_rooms