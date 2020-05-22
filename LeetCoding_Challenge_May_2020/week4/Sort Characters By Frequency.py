from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        
        x=Counter(s)
        st=""
        
        for i in x.most_common():
            st+=i[0]*i[1]
            
        return st
        
        
#added coorect time completxity.
#counter will inturn use max heap to get the most common elements
