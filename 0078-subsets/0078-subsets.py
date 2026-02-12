class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        total_subset=1<<n
        res=[]
        for num in range(0,total_subset):
            lst=[]
            for i in range(0,n):
                if num &(1<<i)!=0:
                    lst.append(nums[i])

            res.append(lst)
        return res