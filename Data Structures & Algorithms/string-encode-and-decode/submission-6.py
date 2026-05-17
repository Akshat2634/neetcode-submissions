class Solution:

    def encode(self, strs: List[str]) -> str:
        
        new_str = ""
        for st in strs:
            siz = len(st)
            new_str += str(siz) + "#" + st

        print(new_str)
        return new_str

    def decode(self, s: str) -> List[str]:

        # "4#neet"

        i = 0 
        n = len(s)
        ans = []

        while i<n:
            j=i

            while(s[j]!="#"):
                j=j+1
            
            size = int(s[i:j])

            j=j+1

            word = s[j:j+size]
            ans.append(word)

            i = j+size
        return ans
