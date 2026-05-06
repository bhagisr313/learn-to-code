# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans
#can be solved as nums + nums as well

# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in nums:
            if i not in my_set:
                my_set.add(i)
            else:
                return True
        return False
# can be solved using brute force as well but that would be O(n^2) time complexity, using a set gives us O(n) time complexity and O(n) space complexity

# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}

        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in my_dict:
                    my_dict[i] += 1
                else:
                    my_dict[i] = 1
            for j in t:
                if j in my_dict:
                    my_dict[j] -= 1
                else:
                    return False
            for k,v in my_dict.items():
                if v != 0:
                    return False
        return True
# compared the length before processing, kept adding the character to disctionary, for the first string and removing the character for second string, if any char is not found return false in else. In last iterate through dict and check if the value is true for all keys, if not return false annd return true in the end outside the for loops. /// can use, counter(s) == counter(t) for one line code.
