class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
            

""""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) != len(nums)
        
a set only lists unique elements. 
so when we check the length of nums using set, 
it will not match the length of nums is a element is repeated.
"""