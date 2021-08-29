class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev =0
        y = str(x)       
        if(y[0] == '-'):
            y = y[1::]
            rev = int('-'+ y[-1::-1])
            if(rev > (-2**32)/2 and rev < (2**32)/2-1):
                return rev
            else:
                return 0
        else:
            while(x > 0 ):
                rem = x%10
                rev = rev*10 + rem
                x = x/10 
            if(rev > (-2**32)/2 and rev < (2**32)/2-1):
                return rev
            else:
                return 0