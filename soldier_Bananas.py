"""
Solution
input the values where k = first dollar ,
mon = money at hand , t = target bananas
use t to iterate while nuultipying the k with for range of t
during each iteration store the sum
after loop , find difference between sum and mon
if difference is less or = 0 , print 0 , else print diff
"""

k, mon, t = map(int, input().split())
sum = 0
for i in range(1, t + 1):
    new = k * i
    sum += new
diff = sum - mon
if diff <= 0:
    print(0)
else:
    print(diff)
