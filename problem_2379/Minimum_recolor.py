class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=len(blocks)
        count_b=0
        c=0
        for i in range(count-k+1):
            text=blocks[i:(i+k)]
            for j in text:
                if j=='B':
                    c+=1
            if c>count_b:
                count_b=c
            if count_b==k:
                break
            c=0
        n=k-count_b
        return n