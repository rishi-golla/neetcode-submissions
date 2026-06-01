class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        if len(s) != len(t): # return false if the are not the same length
            return False

        for index in range(len(s)):
            countS[s[index]] = countS.get(s[index], 0) + 1
            countT[t[index]] = countT.get(t[index], 0) + 1

        if countS == countT:
            return True

        return False