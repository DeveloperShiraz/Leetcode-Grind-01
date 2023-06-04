class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def recursive_func(i,j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return 1 + recursive_func(i-1, j-1)
            else:
                return max(recursive_func(i-1,j), recursive_func(i,j-1))
        return recursive_func(len(text1)-1,len(text2)-1)