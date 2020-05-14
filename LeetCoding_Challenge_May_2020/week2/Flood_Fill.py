class Solution:
    visited=[]
    img=[]
    def fill(self, sr, sc, newColour, oldColour):
        if sr<0 or sr>=len(self.img) or sc<0 or sc>=len(self.img[0]):
            return
        
        #print(sr,sc)
        if self.visited[sr][sc]=='#':
            return
        
        self.visited[sr][sc]='#'
        
        if self.img[sr][sc]==oldColour:
            self.img[sr][sc]=newColour
        else:
            return
        
        
        self.fill(sr+1, sc, newColour, oldColour)
        self.fill(sr, sc+1, newColour, oldColour)
        self.fill(sr-1, sc, newColour, oldColour)
        self.fill(sr, sc-1, newColour, oldColour)
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.visited=[[0 for x in range(len(image[0]))] for y in range(len(image))]
        self.img = image
        self.fill(sr, sc, newColor, image[sr][sc])
        return self.img
