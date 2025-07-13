import collections

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + nums[i - 1]
        
        f = [0] * (n + 1)
        dp = [0] * (n + 1)
        dq = collections.deque()
        dq.append(0)
        
        for i in range(1, n + 1):
            while len(dq) >= 2:
                if f[dq[1]] + s[dq[1]] <= s[i]:
                    dq.popleft()
                else:
                    break
            
            best_j = dq[0]
            dp[i] = dp[best_j] + 1
            f[i] = s[i] - s[best_j]
            
            while dq and f[dq[-1]] + s[dq[-1]] >= f[i] + s[i]:
                dq.pop()
            dq.append(i)
        
        return dp[n]