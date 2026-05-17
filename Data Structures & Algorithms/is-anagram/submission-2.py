class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        new_s = sorted(s)
        new_t = sorted(t)

        return new_s==new_t
        