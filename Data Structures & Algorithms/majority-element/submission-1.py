class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for idx, num in enumerate(nums):
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        print(hash_map)
        key,val = 0,0
        for i in hash_map:
            if hash_map[i] > val:
                key,val = i,hash_map[i]
        
        return key
            

