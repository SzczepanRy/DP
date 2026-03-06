

class Solution:
    def wordBreak(self, s, wordDict ) :
        n = len(s)

        dp= [False] *(n+1)
        dp[0] = True

        # l is the length of the string beeing constdered
        for l in range(1,n+1 ):
            for i in range(l):
                if dp[i] and s[i:l] in wordDict:
                    dp[l]= True
                    break
        return dp[len(s)]



s =Solution()
st = "applepenapple"
wordDict = ["apple","pen"]
print(s.wordBreak(st, wordDict))

