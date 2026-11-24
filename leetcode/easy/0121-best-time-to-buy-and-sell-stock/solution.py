class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maximum=0
        minimum=float('inf')
        for price in prices:
            if price<minimum:
                minimum=price
            elif price-minimum>maximum:
                maximum=price-minimum
        return maximum