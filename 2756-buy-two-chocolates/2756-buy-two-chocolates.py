import math
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        sorted_prices = sorted(prices)

        smallest_total = sorted_prices[0] + sorted_prices[1]

        if smallest_total <= money:
            return money - smallest_total
        
        return money

        

        