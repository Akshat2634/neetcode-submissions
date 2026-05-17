class Solution:

    def encode(self, strs: List[str]) -> str:
        # - num#string
        s = ""
        for n_str in strs:
            length = len(n_str)
            s += str(length) + '#' + n_str

        return s


    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []

        while i<len(s):
            j=i

            while(s[j]!='#'):
                j+=1
            size = int(s[i:j])

            j=j+1

            word = s[j:j+size]
            ans.append(word)

            i = j+size
        return ans

