class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        length = len(nums)
        k = 0
        for idx,num in enumerate(nums):
            if num == val:
                #swap

                #find next not val num
                for i in range(idx+1, length):
                    if nums[i] != val:
                        nums[i], nums[idx] = nums[idx], nums[i]
                        k += 1
                        break
            else:
                k += 1

        return k

        # k = 0
        # for num in nums:
        #     if num != val:
        #         k += 1

        # return nums[:k]
                    



