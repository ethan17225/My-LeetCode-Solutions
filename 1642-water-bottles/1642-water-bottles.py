class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottle = numBottles
        remain_bottle = numBottles

        while remain_bottle//numExchange != 0:
            exchange_bottle = remain_bottle // numExchange
            remain_bottle = remain_bottle - exchange_bottle*numExchange + exchange_bottle
            total_bottle += exchange_bottle

        return total_bottle