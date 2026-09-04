class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit=0
        min_price = prices[0]

        for price in prices:
            if price<min_price:
                min_price=price
            profit=price-min_price
            if profit > max_profit:
                max_profit=profit
        return max_profit
        
        
        # min_buy = min(prices)
        # max_sell = max(prices)
        # for num  in prices[1:]:
        #     if num > max_sell:
        #         max_sell=num
        #     else:
        #         continue
        # return max_sell-min(prices)

        # min_price = float('inf')
        # max_profit = 0
        
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > max_profit:
        #         max_profit = price - min_price
        # return max_profit