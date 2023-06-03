class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def recursive_func(i):
            if i == 0:
                return 1
            else:
                mod = 1
                for ind in range(i):
                    if nums[i] > nums[ind]:
                        mod = max(mod, 1+recursive_func(ind))
            return mod
        return max(recursive_func(i) for i in range(len(nums)))