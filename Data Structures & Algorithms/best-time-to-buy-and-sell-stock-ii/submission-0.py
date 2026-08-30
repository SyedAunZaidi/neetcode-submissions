class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        bought = False
        buy_idx = 0
        le = len(prices)

        for i in range(le):

            if bought: #bought = True
                if i != le-1:

                    if prices[i] > prices[i+1]:
                        #sell
                        profit = profit + (prices[i] - prices[buy_idx])
                        bought = False
                else:
                    profit = profit + (prices[i] - prices[buy_idx])
                    bought = False

            else: #bought = False
                if i != le-1:

                    if prices[i] < prices[i+1]: #tomorrow is higher
                        #buy
                        buy_idx = i
                        bought = True
                    # else: #tomorrow is lower
                    #     #don't buy
                    #     continue
                else:
                    continue
        return profit


