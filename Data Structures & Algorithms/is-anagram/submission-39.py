class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        len_s, len_t = len(s), len(t)

        if len_s != len_t:
            return False

        hm_s, hm_t = {}, {}
        for char in s:
            if char in hm_s:
                hm_s[char] += 1
            else:
                hm_s[char] = 1

        for char in t:
            if char in hm_t:
                hm_t[char] += 1
            else:
                hm_t[char] = 1

        if hm_s == hm_t:
            return True
        return False