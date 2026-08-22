class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        leng = len(nums)

        arr = 2*leng*[0]

        for idx,val in enumerate(nums):
            arr[idx]= nums[idx]
            arr[idx+leng]=nums[idx]

        return arr

        