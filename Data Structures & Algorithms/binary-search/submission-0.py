class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0,len(nums)-1

        while left<=right:
            med = (left+right)//2

            if nums[med]==target:
                return med
            elif nums[med]>target:
                right = med - 1
            elif nums[med]<target:
                left = med + 1

        return -1

            

        