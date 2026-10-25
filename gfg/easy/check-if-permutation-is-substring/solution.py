from collections import Counter
class Solution:
    def search(self, txt, pat):
        left=0
        k=len(pat)
        patc={}
        winc={}
        for i in pat:
            if i in patc:
                patc[i]+=1
            else:
                patc[i]=1
        for right in range(len(txt)):
            if txt[right] in winc:
                winc[txt[right]]+=1
            else:
                winc[txt[right]]=1
            if right-left+1>k:
                winc[txt[left]]-=1
                if winc[txt[left]]==0:
                    del winc[txt[left]]
                left+=1
            if right-left+1==k:
                if winc==patc:
                    return True
        return False
            
            
        