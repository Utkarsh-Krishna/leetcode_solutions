class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<=2:
            return True
        
        x1=coordinates[0][0]
        y1=coordinates[0][1]
        x2=coordinates[1][0]
        y2=coordinates[1][1]
        
        if x2-x1==0:
            slope=-1
        else:
            slope=(y2-y1)/(x2-x1)
        #print(slope)
        for i in range(1, len(coordinates)-1):
            x1=coordinates[i][0]
            y1=coordinates[i][1]
            x2=coordinates[i+1][0]
            y2=coordinates[i+1][1]
            
            if x2-x1==0:
                nslope=-1
            else:
                nslope=(y2-y1)/(x2-x1)
            
            if nslope!=slope:
                return False
        
        return True
