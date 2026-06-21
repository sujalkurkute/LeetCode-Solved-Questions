class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
           s = 0
           for j in range(i,n):
               s+=nums[j]

               if str(s)[0]==str(x) and str(s)[-1]==str(x):
                   ans+=1
        return ans