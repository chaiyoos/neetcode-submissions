class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums=nums
        self.target=target
        ml={}
        for i, value in enumerate(nums):
            diff=target-value
            if diff in ml:
                return [ml[diff],i]
            ml[value]=i
            
            



