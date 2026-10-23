class Solution:
    def rotate(self, arr: list[int]) -> None:
        arr[:]=arr[len(arr)-1:]+arr[:len(arr)-1]
        return arr