class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        stack = []
        brackets = {')' : '(', ']':'[', '}':'{'}
        if len(s_list) % 2 != 0:
            return False
        
        for bracket in s_list:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if stack and brackets[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True
