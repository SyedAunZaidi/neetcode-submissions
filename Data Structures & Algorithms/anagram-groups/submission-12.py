class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}
        
        for string in strs:

            freq_dic = {}

            # creating frequency dict
            for char in string:
                if char in freq_dic:
                    freq_dic[char] += 1
                else:
                    freq_dic[char] = 1
            
            # creating fingerprint
            arr = 26 * [0]
            for key in freq_dic:
                idx = ord(key) - 97
                arr[idx] = freq_dic[key]
            fingerprint = tuple(arr)


            if fingerprint not in hash_map:
                hash_map[fingerprint] = [string]
            else: #fingerprint exists
                hash_map[fingerprint].append(string)

        answer = []
        for key in hash_map:
            answer.append(hash_map[key])
        return answer

