class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        for k in range(1, length):
            for i in range(1, length):

                if nums[i] < nums[i-1]:
                    #swap
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            
        #     print(nums)


        # print(nums)