
# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 
  
print (shout('Hello')) 
  
yell = shout 
  
print (yell('Hello')) 

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i]==nums[i-1]):
                 return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        