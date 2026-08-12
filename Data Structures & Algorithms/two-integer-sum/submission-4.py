class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = list()
        for i in range (len(nums)) :
            for j in range (len(nums)):
                if (i != j ) :
                    if  (nums [i] + nums [j] == target) :
                        if not (i in out) and not (j in out):
                            out.append(i)
                            out.append(j)
                        
        sorted (out)
        return out 

