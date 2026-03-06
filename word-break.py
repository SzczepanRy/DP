class Solution:
    def wordBreak(self, s, wordDict ) :

        res= 0

        def wordcheck(s ,sea):
            n = len(s)
            for i in range(len(sea) - n +1):
                if sea[i:i+n] == s:
                    t1= sea[:i+1]
                    t2= sea[i+n-1:]
                    sea=t1+t2
                    return (True, sea)
            return (False, sea)

        for st in wordDict:
            print(s)
            vals =wordcheck(st, s)
            if vals[0]:
                s= vals[1]
                res+=1
            else:
                return False

        print(res)
        if res == len(wordDict):
            return True
        return False


s =Solution()
st = "applepenapple"
wordDict = ["apple","pen"]
print(s.wordBreak(st, wordDict))

