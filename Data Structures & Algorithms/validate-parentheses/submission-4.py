class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        n = len(s)
        

        for st in s:
            if st == '[' or st=='{' or st=='(':
                stk.append(st)

            elif stk and (
                (st == ']' and stk[-1] == '[') or
                (st == '}' and stk[-1] == '{') or
                (st == ')' and stk[-1] == '(')
            ):
                stk.pop()
            else:
                return False
        return len(stk)==0