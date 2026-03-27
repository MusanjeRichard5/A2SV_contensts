n, t = map(int, input().split())
arr_n = list(map(int, input().split()))
# arr_n.sort()
left = 0
right = n - 1
current_sum = 0
max_window = 0

for right in range(n):
    current_sum += arr_n[right]

    while current_sum > t:
        current_sum -= arr_n[left]
        left += 1
    max_window = max(max_window, right - left + 1)

print(max_window)
