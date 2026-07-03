class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        dict_s = dict()
        dict_t = dict()

        for index in range(len_s):
            if s[index] not in dict_s:
                dict_s[s[index]] = 1
            else:
                dict_s[s[index]] += 1
    
            if t[index] not in dict_t:
                dict_t[t[index]] = 1
            else:
                dict_t[t[index]] += 1 

        for key in dict_s:
            if key not in dict_t:
                return False
            else:
                if dict_s[key] != dict_t[key]:
                    return False
  



        return True