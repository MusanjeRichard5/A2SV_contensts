""" "Approach
use two pointers
left pointer in one arr and right pointer in another array
"""

n, m = map(int, input().split())
n_arr = list(map(int, input().split()))
m_arr = list(map(int, input().split()))
output = []
i = 0
j = 0
# n = 6
# m = 7
# n_arr = [1, 6, 9, 13, 18, 18]
# m_arr = [2, 3, 8, 13, 15, 21, 25]
while i < n and j < m:
    left = n_arr[i]
    right = m_arr[j]
    if left < right:
        output.append(left)
        i += 1
    else:
        output.append(right)
        j += 1

output.extend(n_arr[i:])

output.extend(m_arr[j:])
print(*output)
