import math

MOD = 10**9 + 7

class Solution(object):
    def idealArrays(self, n, maxValue):
        max_k = min(n, 14)
        dp = [[0] * (maxValue + 1) for _ in range(max_k + 1)]
        for v in range(1, maxValue + 1):
            dp[1][v] = 1
        for k in range(2, max_k + 1):
            for v in range(1, maxValue + 1):
                for m in range(2, maxValue // v + 1):
                    dp[k][v * m] = (dp[k][v * m] + dp[k - 1][v]) % MOD
        comb = [[0] * (max_k + 1) for _ in range(n + 1)]
        comb[0][0] = 1
        for i in range(1, n + 1):
            comb[i][0] = 1
            for j in range(1, max_k + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
        res = 0
        for k in range(1, max_k + 1):
            total = 0
            for v in range(1, maxValue + 1):
                total = (total + dp[k][v]) % MOD
            res = (res + total * comb[n - 1][k - 1]) % MOD
        return res
