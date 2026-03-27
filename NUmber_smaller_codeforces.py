n, m = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

left = 0
output = []

for right in range(m):

    while left < n and arr_n[left] < arr_m[right]:
        left += 1
    output.append(left)
print(*output)
