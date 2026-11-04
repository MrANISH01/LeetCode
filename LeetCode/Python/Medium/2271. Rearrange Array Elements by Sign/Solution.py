class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        len1=len(nums)
        lst2=[]
        lst3=[]
        

        for i in nums:
            if i>0:
                lst2.append(i)
            else:
                lst3.append(i)
        len2 = len(lst2)
        len3 = len(lst3)
        res=[]
        i=0
        j=0
        

        while i<len2 and j<len3:
            res.append(lst2[i])
            res.append(lst3[j])
            i+=1
            j+=1

        return res


        

        