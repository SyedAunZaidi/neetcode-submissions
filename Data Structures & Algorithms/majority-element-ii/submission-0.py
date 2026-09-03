class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        length = len(nums)
        bar = length/3
        freq = {}
        answer = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq:
            if freq[num] > bar: 
                answer.append(num)
        return answer
        