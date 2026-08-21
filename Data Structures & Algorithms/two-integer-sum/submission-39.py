class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for idx, val in enumerate(nums):
            key = target - val
            if val in hm:
                return [hm[val], idx]
            else:
                hm[key] = idx
            
        return False