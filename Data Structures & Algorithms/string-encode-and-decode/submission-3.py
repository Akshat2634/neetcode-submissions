class Solution:

    def encode(self, strs: List[str]) -> str:
        
        new_str = ""
        for st in strs:
            size = len(st)
            new_str += str(size) + '#' + st

        return new_str


    def decode(self, s: str) -> List[str]:

        i=0
        ans = []

        while(i<len(s)):
            j=i

            while(s[j]!='#'):
                j+=1

            size = int(s[i:j])
            j+=1

            word = s[j:j+size]
            ans.append(word)

            i = j+size
        return ans


