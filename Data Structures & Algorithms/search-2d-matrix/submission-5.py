class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, row_len = 0, len(matrix) -1
        final_row = None

        if row_len > 0:

            while top < row_len:

                med = (top+row_len) // 2
                print(f"Searching in matrix row {med}, target = {target}")

                # if matrix[med][-1] == target:
                #     return True
                if matrix[med][-1] >= target:
                    row_len = med
                elif matrix[med][-1] < target:
                    top = med+1

                if top==row_len:
                    final_row = top
                    print(f"found row : {final_row}")
            
            if final_row == None:
                return False
        else:
            final_row = 0
        
        #search col

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            med = (left+right)//2

            print(f"Searching in matrix row {final_row}, col {med}, value{matrix[final_row][med]}, target = {target}")


            if matrix[final_row][med] == target:
                return True
            elif matrix[final_row][med] > target:
                right = med - 1
            elif matrix[final_row][med] < target:
                left = med + 1

        
        return False



