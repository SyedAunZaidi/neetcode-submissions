class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        len_s, len_t = len(s), len(t)

        if len_s != len_t:
            return False

        hm_s, hm_t = {}, {}

        for idx in range(len_s):
            if s[idx] in hm_s:
                hm_s[s[idx]] += 1
            else:
                hm_s[s[idx]] = 1

            if t[idx] in hm_t:
                hm_t[t[idx]] += 1
            else:
                hm_t[t[idx]] = 1


        if hm_s == hm_t:
            return True
        return False