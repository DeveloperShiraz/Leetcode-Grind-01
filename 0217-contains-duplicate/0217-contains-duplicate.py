class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Game Plan.
        # 1. create a hashmap. Loop over array indexes one by one and check if the value is in hashmap.
        # 2. if i can't find the value in there. Add it in the hashmap.
        # 3. if the value is found then return true.
        # 4. this takes O(n) space complexity and the runtime is O(n) as well.
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False