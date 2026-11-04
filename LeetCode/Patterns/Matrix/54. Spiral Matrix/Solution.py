class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        m = len(matrix[0])

        left = 0 
        right = m-1
        top=0
        bottom = n-1

        res=[]
        
        while(top<=bottom and left <=right):



        # left dekhi right samma
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1

            #right dekhi bottom samma

            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -=1

            #right dekhi left bottom
            if(top <= bottom):
                i=right
                while(i>=left):
                    res.append(matrix[bottom][i])
                    i-=1
                bottom -=1

            #bottom to top samma
            if(left <= right):
                i = bottom
                while(i>=top):
                    res.append(matrix[i][left])
                    i-=1
                left +=1

        return res



        
         

        