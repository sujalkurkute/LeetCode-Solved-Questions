from typing import List

class Solution:
    
    def solve(self, index: int, total: int, subset: List[int], 
              nums: List[int], target: int, result: List[List[int]]) -> None:
        
        # Base Case: if total equals target
        if total == target:
            result.append(subset.copy())
            return
        
        # If total exceeds target or index out of range
        if total > target or index >= len(nums):
            return
        
        # ✅ Include current element (we can reuse same index)
        subset.append(nums[index])
        self.solve(index, total + nums[index], subset, nums, target, result)
        
        # Backtrack (remove last element)
        subset.pop()
        
        # ❌ Exclude current element (move to next index)
        self.solve(index + 1, total, subset, nums, target, result)
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result