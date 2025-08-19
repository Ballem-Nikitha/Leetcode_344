class Solution:
    def check(self, nums: List[int]) -> bool:
        s=nums.copy()
        s.sort()
        for i in range(len(nums)):
            s1=s[i:]+s[:i]
            if s1==nums:
                return True
        else:
            return False