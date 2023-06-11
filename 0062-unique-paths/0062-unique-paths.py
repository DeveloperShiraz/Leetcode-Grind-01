class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(m_dup, n_dup):
            if m_dup == m-1 or n_dup == n-1: return 1
            return helper(m_dup+1,n_dup)+helper(m_dup,n_dup+1)
        return helper(0,0)