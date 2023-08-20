class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasharray ={}
        for i,n in enumerate(nums):
            value = target-n
            if value in hasharray:
                return [hasharray[value],i]
            hasharray[n]=i
        return