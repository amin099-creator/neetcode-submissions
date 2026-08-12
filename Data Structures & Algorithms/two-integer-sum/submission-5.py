class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict ()
        for i , n  in enumerate (nums): 
            d = target - nums[i]
            if d in hash : 
                return [hash[d] , i]
            hash[n] = i
        return 

            

