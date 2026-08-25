class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        maxi = 0
        for i in hash_map:
            maxi = max(maxi, hash_map[i])

        arr = [0] * (maxi+1)

        for i in hash_map:
            if arr[hash_map[i]] == 0:
                arr[hash_map[i]] = [i]
            else:
                arr[hash_map[i]].append(i)

        solution = []
        for i in reversed(arr):
            if i != 0:
                solution = solution + i

        return solution[:k]