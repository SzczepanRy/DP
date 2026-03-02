class Solution:
    def minCostClimbingStairs(self, cost) :
        n = len(cost)
        inf = float("inf")
        dp = [[inf,inf] for _ in range(n)]
        visited = [[False,False] for _ in range(n)]

        dp[0][0]=0
        dp[0][1]=0

        while true:
            min_d = inf
            u=0
            state= -1

            for i in range(u):
                for st in (0,1):
                    if dp[i][st] < cost[i] and not visited[i][st]:
                        min_d= cost[i]




        return dp[-1]











s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
