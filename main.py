# https://leetcode.com/problems/build-array-from-permutation/

def build_array(nums):
    ans = []

    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    
    return ans

print(build_array([0,2,1,5,3,4]))
print(build_array([5,0,1,2,3,4]))

# -----------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])
    
        return ans