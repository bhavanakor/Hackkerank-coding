class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ps=0
        pe=len(numbers)-1
        for i in range(len(numbers)):
            if numbers[ps]+numbers[pe]==target:
                return [ps+1,pe+1]
            elif numbers[ps]+numbers[pe]>target:
                pe-=1
            elif numbers[ps]+numbers[pe]<target:
                ps+=1
        return [ps+1,pe+1]
        