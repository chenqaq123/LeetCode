"""
思路：使用堆栈记录前一个括号类型，然后与后一个匹配即可，相当于用堆栈解析算式的简化版
"""

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dicts = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []
        keys = bracket_dicts.keys()
        for c in s:
            if c in keys:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                c_left = stack.pop()
                if c != bracket_dicts[c_left]:
                    return False
        return (len(stack)==0)
                