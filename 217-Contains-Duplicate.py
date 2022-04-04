class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

  
# 2 more Solutions


# runtime: O(nlogn) space: O(1)
def containsDuplicate(array):
    array.sort()
    for i in range(1, len(array)):
        prevElement = array[i-1]
        presentElement = array[i]
        if prevElement == presentElement:
            return True
    return False

# runtime: O(n)  space: O(1)
def containsDuplicate(array):
    return len(set(array)) == len(array)

