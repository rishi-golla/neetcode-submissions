class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for letter in s:
            map1[letter] = map1.get(letter, 0) + 1

        for aksharam in t:
            map2[aksharam] = map2.get(aksharam, 0) + 1

        if map1 == map2:
            return True
        
        return False