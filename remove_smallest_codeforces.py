"""
Approach first sort the elements
compare consecutive elements
if there difference is greater than one
return no
else
return yes
"""

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print("YES")
        continue
    else:
        arr.sort()
        flag = True
        for i in range(n - 1):
            if abs(arr[i] - arr[i + 1]) > 1:
                flag = False
                break

        if flag:
            print("YES")
        else:
            print("NO")
