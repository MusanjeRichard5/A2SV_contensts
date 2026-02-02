class Solution:
    def checkEqual(self, a, b) -> bool:
        #sort them first
        a.sort()
        b.sort()
        for i in range (0,len(a)):
            if a[i] == b[i]:
                continue
            else:
                return False
        return True
