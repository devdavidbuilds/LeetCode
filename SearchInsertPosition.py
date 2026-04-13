class Solution(object):
    
    def fetchIndex(self,nums,target):
        for i,val in enumerate(nums):
            if val==target:
                return i
    def searchInsert(self, nums, target):
    
        if target in nums:
            index=self.fetchIndex(nums,target)
            return index
        else :
            nums.append(target)
            nums.sort()
            index=self.fetchIndex(nums,target)
            return index
 
            
     
