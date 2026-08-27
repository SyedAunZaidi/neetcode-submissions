class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_mul, right_mul = {}, {}

        n = len(nums)
        
        l_m, r_m = 1,1
        for i, j in zip(range(n), range(n-1,-1,-1)):
            l_m *= nums[i]
            left_mul[i] = l_m

            r_m *= nums[j]
            right_mul[j] = r_m
        
        arr = []
        for i in range(n):
            if i-1 < 0:
                arr.append(1*right_mul[i+1])
            elif i+1 >= n:
                arr.append(left_mul[i-1]*1)
            else:
                arr.append(left_mul[i-1]*right_mul[i+1])
        
        return arr


            

