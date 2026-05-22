class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict1 = {}
        my_dict2 = {}

        for char in s:
            if char in my_dict1:
                my_dict1[char] += 1
            else:
                my_dict1[char] = 1
        
        for char in t:
            if char in my_dict2:
                my_dict2[char] += 1
            else:
                my_dict2[char] = 1

        return my_dict1 == my_dict2
                
            