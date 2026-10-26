class Solution:
    def hasTripletSum(self, arr, target):
        for i in range(len(arr)):
            find=set()
            for j in range(i+1,len(arr)):
                x=target-arr[i]-arr[j]
                if x in find:
                    return True
                find.add(arr[j])
        return False
            