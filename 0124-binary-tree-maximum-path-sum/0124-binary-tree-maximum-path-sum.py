class Solution:
    def maxPathSum(self, root):
        maxi = float('-inf')

        def solve(node):
            nonlocal maxi
            
            if node is None:
                return 0

            leftSum = solve(node.left)
            if leftSum < 0:
                leftSum = 0

            rightSum = solve(node.right)
            if rightSum < 0:
                rightSum = 0

            #  Update global maximum
            maxi = max(maxi, node.val + leftSum + rightSum)

            #  Return path sum including current node
            return node.val + max(leftSum, rightSum)

        solve(root)
        return maxi