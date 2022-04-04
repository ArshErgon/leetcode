class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

    
    
#   3 more solutions


# O(nlogn) runtime, space: O(nm); where n is str1 and m is str2 // or just O(n)
def validAnagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    newStr1 = sorted(str1)
    newStr2 = sorted(str2)

    for i in range(len(newStr1)):
        if newStr1[i] != newStr2[i]:
            return False
    
    return True

print(validAnagrams('cat', 'tac'))


# O(n) with O(1) because we will be getting lower case english letters
# 26 characters
def validAnagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    hashMap = dict()
    for i in str1:
        hashMap[i] = 1 + hashMap.get(i, 0)


    for i in str2:
        if i in hashMap:
            hashMap[i] -= 1
        else:
            return False

    for i in str1:
        if hashMap[i] != 0:
            return  False

    return True

print(validAnagrams('cat', 'tca'))    


# O(n) with O(1) because we will be getting lower case english letters
# 26 characters
def validAnagrams(str1, str2):
    charArr = [0] * 26

    for i in str1:
        charArr[ord(i) - ord('a')] += 1

    
    for i in str2:
        pos = ord(i) - ord('a')
        if charArr[pos] == 0:
            return False

    return True


print(validAnagrams('cat', 'tca'))
