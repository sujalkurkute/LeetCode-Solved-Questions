class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        
        longest=0
        for num in s:
            if num-1 not in s:
                x=num
                count=1
                while x+1 in s:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest

