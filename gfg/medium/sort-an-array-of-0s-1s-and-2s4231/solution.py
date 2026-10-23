class Solution:
    def sort012(self, arr):
        zero=[]
        one=[]
        two=[]
        for element in arr:
            if element==0:
                zero.append(element)
            if element==1:
                one.append(element)
            if element==2:
                two.append(element)
        result=zero+one+two
        arr[:]=result
        return arr