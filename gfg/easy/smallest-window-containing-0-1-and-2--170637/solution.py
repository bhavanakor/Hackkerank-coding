class Solution:
    def smallestSubstring(self, s):
        seen={'0':-1,'1':-1,'2':-1}
        left=0
        min_len=float('inf')
        for right in range(len(s)):
            seen[s[right]]=right
            if seen['0']!=-1 and seen['1']!=-1 and seen['2']!=-1:
                left=min(seen['0'],seen['1'],seen['2'])
                current=right-left+1
                min_len=min(min_len,current)
        return min_len if min_len!=float('inf') else -1