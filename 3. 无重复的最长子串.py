class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            52ms
            85.71%
        """
        if s is None or len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        max_length = 0
        current_substring = ""

        for i in range(len(s)):
            if s[i] in current_substring:
                if len(current_substring) > max_length:
                    max_length = len(current_substring)
                current_substring = current_substring[current_substring.index(s[i]) + 1:]

            current_substring += s[i]

        if len(current_substring) > max_length:
            max_length = len(current_substring)

        return max_length


if __name__ == '__main__':
    s = "pwwkew"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)