class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = dict()
        for idx, val in enumerate(nums):
            print(hashmap)

            tt = target - val
            if tt in hashmap:
                return [hashmap[tt], idx]
            else:
                hashmap[val] = idx
        
