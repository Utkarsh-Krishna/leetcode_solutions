# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        mid=n//2
        l=1
        r=n
        lastBad=mid
        while l<=r:
            mid=(l+r)//2
            if isBadVersion(mid):
                lastBad=mid
                r=mid-1
            else:
                l=mid+1
        
        return lastBad
