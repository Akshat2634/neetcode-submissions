"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meet_start = sorted(i.start for i in intervals)
        meet_end = sorted(i.end for i in intervals)

        s= 0 
        e=0
        rooms = 0
        min_rooms = 0

        while s<len(meet_start):
            if meet_start[s]< meet_end[e]:
                rooms+=1
                s+=1
            else:
                rooms-=1
                e+=1
            min_rooms = max(rooms,min_rooms)
        return min_rooms

        