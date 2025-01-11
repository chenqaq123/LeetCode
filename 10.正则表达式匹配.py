class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # solution2: 从后往前匹配规律
        def match(state, char):
            """检测一个字符是否匹配对应的状态"""
            if state[0] == ".":
                return True
            else:
                return char==state[0]
        
        states = []
        min_chars = []
        
        # 解析规律p对应的所有状态
        i = 0
        while i < len(p):
            if p[i] == "*":
                raise ValueError("The rule p is not correct!")
            if i+1 < len(p) and p[i+1] == "*":
                states.append(p[i:i+2])
                min_chars.append(0)
                i += 2
            else:
                states.append(p[i:i+1])
                min_chars.append(1)
                i += 1
        
        # 尝试将字符串匹配到对应的状态
        matched_chars = [''] * len(states)
        i = j = 0
        while j < len(s):
            if i >= len(states):
                i -= 1 
                while i >= 0  and ((min_chars[i]==1 and len(matched_chars[i])>=1) or not match(states[i], s[j])):
                    j -= len(matched_chars[i])
                    matched_chars[i] = ""
                    i -= 1
                if i < 0:
                    return False
                else:
                    matched_chars[i] += s[j]
                    i += 1
                    j += 1
                continue
            while min_chars[i] == 0 and i+1 < len(states):
                i += 1
            if match(states[i], s[j]):
                matched_chars[i] += s[j]
                i += 1
                j += 1
            else:
                j -= len(matched_chars[i])
                matched_chars[i] = ""
                i -= 1
                while i >= 0  and ((min_chars[i]==1 and len(matched_chars[i])>=1) or not match(states[i], s[j])):
                    j -= len(matched_chars[i])
                    matched_chars[i] = ""
                    i -= 1
                if i < 0:
                    return False
                else:
                    matched_chars[i] += s[j]
                    i += 1
                    j += 1
        if sum(min_chars[i:]) > 0:
            return False
        return True
    
if __name__ == "__main__":
    print(Solution().isMatch("aaba", "ab*a*c*a"))