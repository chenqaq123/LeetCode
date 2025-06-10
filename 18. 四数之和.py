from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        i_last = j_last = None
        for i in range(len(nums)):
            if i_last is not None and nums[i] == i_last:
                continue
            i_last = nums[i]
            for j in range(i+1, len(nums)):
                if j_last is not None and nums[j] == j_last:
                    continue
                j_last = nums[j]
                m = j+1
                n = len(nums)-1
                while m < n:
                    while m<n and nums[i]+nums[j]+nums[m]+nums[n]<target:
                        m += 1
                    while m<n and nums[i]+nums[j]+nums[m]+nums[n]>target:
                        n -= 1
                    if m >= n:
                        break
                    if nums[i]+nums[j]+nums[m]+nums[n]==target:
                        results.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        while m < n and nums[m] == nums[m-1]:
                            m += 1
                
            j_last = None

        return results

Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0)