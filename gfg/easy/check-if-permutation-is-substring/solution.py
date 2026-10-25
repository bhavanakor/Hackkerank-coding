from collections import Counter
class Solution:
    def search(self, txt, pat):
        left=0
        k=len(pat)
        patc=Counter(pat)
        winc=Counter()
        for right in range(len(txt)):
            winc[txt[right]]+=1
            if right-left+1>k:
                winc[txt[left]]-=1
                left+=1
            if right-left+1==k:
                if winc==patc:
                    return True
        return False
            
            
        