class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left = 0
        right = matrix[0].__len__()
        top = 0
        bottom = matrix.__len__()
        
        to_explore = matrix.__len__() * matrix[0].__len__()
        to_ret = []
        
        while(True):
            
            for a in range(left , right):
                to_ret.append(matrix[top][a])
                to_explore -= 1
            top += 1
            if to_explore == 0:
                break
            for b in range(top, bottom):
                to_ret.append(matrix[b][right-1])
                to_explore -= 1
            right -= 1
            if to_explore == 0:
                break
            for c in range(right-1, left-1, -1):
                to_ret.append(matrix[bottom-1][c])
                to_explore -= 1
            bottom -= 1
            if to_explore == 0:
                break
            for d in range(bottom-1, top-1, -1):
                to_ret.append(matrix[d][left])
                to_explore -= 1
            left += 1
            if to_explore == 0:
                break
        
        return to_ret