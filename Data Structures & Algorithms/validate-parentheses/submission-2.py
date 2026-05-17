class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        n = len(s)

        for st in s:
            if st=='[' or st=='{' or st=='(':
                stack.append(st)
            elif stack and (
                (st == ']' and stack[-1] == '[') or
                (st == '}' and stack[-1] == '{') or
                (st == ')' and stack[-1] == '(')
            ):
                stack.pop()
            else:
                return False
        
        if len(stack)==0:
            return True
        return False
        