class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        answer = strs[0]
        g_mini = len(answer)

        leng = len(strs)

        for i in range (0, leng):

            l_mini = min(g_mini, len(strs[i]))
            if l_mini<g_mini:
                g_mini = l_mini

            answer = answer[:l_mini]
            answer_updated = 0

            print(f"answer: {answer}")

            # if strs[i] == answer:
            #     continue
            
            for j in range(g_mini,0,-1):

                print(f"j:{j}, strs[i][:j]:{strs[i][:j]},answer[:j]:{answer[:j]}")

                if strs[i][:j] == answer[:j]:
                    answer = answer[:j]
                    answer_updated = 1
                    g_mini = len(answer)
                    break

        if answer_updated == 0:
            return ""
        else:
            return answer
