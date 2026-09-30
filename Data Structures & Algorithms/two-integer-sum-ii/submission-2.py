class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hashmap = {}

        for idx, val in enumerate(numbers):

            cal = target - val

            if val in hashmap:
                return [hashmap[val]+1, idx+1]

            else:
                hashmap[cal] = idx

        