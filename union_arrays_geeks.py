class Solution:    
    def findUnion(self, a, b):
        a_set = set(a)
        b_set = set(b)
        union = a_set | b_set
        return union
