from collections import Counter
class Solution:
    def search(self, txt, pat):
        left=0
        pat_count=Counter(pat)
        txt_count=Counter()
        size=len(pat)
        for right in range(len(txt)):
            charin=txt[right]
            txt_count[charin]+=1
            if right-left+1 > size:
                charout=txt[left]
                txt_count[charout]-=1
                if txt_count[charout]==0:
                    del txt_count[charout]
                left+=1
            if pat_count==txt_count:
                return True
        return False
            
        