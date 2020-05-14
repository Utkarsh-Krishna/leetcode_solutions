class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid=(l+r)//2
            #print(mid)
            if (mid-1<0 or nums[mid]!=nums[mid-1]) and (mid+1>len(nums)-1 or nums[mid]!=nums[mid+1]):
                return nums[mid]
            
            if mid%2==0:
                if mid+1>=len(nums) or nums[mid]==nums[mid+1]:
                    l=mid+1
                elif mid-1<0 or nums[mid]==nums[mid-1]:
                    r=mid-1
            else:
                if mid+1>=len(nums) or nums[mid]==nums[mid+1]:
                    r=mid-1
                elif mid-1<0 or nums[mid]==nums[mid-1]:
                    l=mid+1
                
                
        return -1
            
            
