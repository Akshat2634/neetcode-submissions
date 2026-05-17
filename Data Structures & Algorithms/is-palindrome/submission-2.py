class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for st in s:
            if st.isalnum():
                new_str+=st.lower()
        
        print(new_str[::-1])
        return new_str == new_str[::-1]