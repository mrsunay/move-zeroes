class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j = len(nums) - 1
        while(i<j):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(j,0)
                j -= 1
            else:
                i += 1
        return nums
        
