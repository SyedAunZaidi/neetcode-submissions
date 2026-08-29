class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        longest = 0

        for num in nums:
            longer = 0
            if num-1 not in freq: #only search start of sequence
                while True:
                    if num in freq:
                        longer += 1
                        num += 1
                    else:
                        break
                longest = max(longest, longer)


        # print(freq,longest)
        return longest
        


        