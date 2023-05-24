class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Here's a way to do it.
        
        hashset = set() #Create a HashSet.
        
        for n in nums: #For loop to go through each value.
            if n in hashset: #if the number n is in hashset
                return True #Returns True
            hashset.add(n) #This is out of the if-statement because as the if-statement on the top only cares about the value which is in the hashset. It ignores the values that are not in the loop. So, This adds the values.
        return False #Finally this returns false.