class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for st in strs:
            new_s = tuple(sorted(st))
            ans[new_s].append(st)

        return list(ans.values())

        