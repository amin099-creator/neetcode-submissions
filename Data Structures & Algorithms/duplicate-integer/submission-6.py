class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if not(i in hashset) :
                hashset.add(i)
            else :
                return True
        return False



