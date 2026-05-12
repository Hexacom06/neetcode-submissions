class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lor, hir = 0, len(matrix)-1
        rlen = len(matrix[0])-1
        r = -1
        while lor <= hir:
            midr = (lor + hir) // 2
            if matrix[midr][0] <= target <= matrix[midr][rlen]: 
                r = midr
                break
            elif matrix[midr][0] > target: hir = midr-1
            else: lor = midr + 1
        
        if r == -1: return False
        
        lo, hi = 0, len(matrix[0])-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[r][mid] == target: return True
            elif matrix[r][mid] < target: lo = mid + 1
            else: hi = mid - 1
        return False