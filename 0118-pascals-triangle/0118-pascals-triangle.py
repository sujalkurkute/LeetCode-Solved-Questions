class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for row in range(numRows):
            current_row=[]

            for col in range(row+1):
                if col==0 or col==row:
                    current_row.append(1)
                else:
                    value=result[row-1][col-1]+result[row-1][col]

                    current_row.append(value)

            result.append(current_row)
        return result