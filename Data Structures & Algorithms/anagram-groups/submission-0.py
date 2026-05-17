class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for st in strs:
            new_st = tuple(sorted(st))
            mp[new_st].append(st)
        
        return list(mp.values())


