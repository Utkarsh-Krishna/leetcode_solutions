class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l=0
        r=len(A)-1
        while l<=r:
            mid=(l+r)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            
            if A[mid]>A[mid+1]:
                r=mid-1
            else:
                l=mid+1
            
