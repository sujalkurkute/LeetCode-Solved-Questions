class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7
        n = len(value)

        # Count all positive terms
        total_pos = 0
        total_sum = 0

        for v, d in zip(value, decay):
            cnt = (v - 1) // d + 1  # terms >= 1
            total_pos += cnt

            # Sum of first cnt terms of AP
            total_sum += cnt * (2 * v - (cnt - 1) * d) // 2

        # If fewer than m positive terms exist, take all of them
        if total_pos <= m:
            return total_sum % MOD

        def count_ge(x):
            cnt = 0
            for v, d in zip(value, decay):
                if v >= x:
                    cnt += (v - x) // d + 1
            return cnt

        # Binary search threshold p
        lo, hi = 1, max(value)

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if count_ge(mid) >= m:
                lo = mid
            else:
                hi = mid - 1

        p = lo

        # Sum all terms > p
        total = 0
        used = 0

        for v, d in zip(value, decay):
            if v > p:
                cnt = (v - (p + 1)) // d + 1

                used += cnt

                total += cnt * (2 * v - (cnt - 1) * d) // 2

        # Fill remaining slots with value p
        total += (m - used) * p

        return total % MOD