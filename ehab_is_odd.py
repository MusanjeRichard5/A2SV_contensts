n = int(input())
arr_n = list(map(int, input().split()))

output = []
even_count = 0
odd_count = 0

for i in range(n):
    if arr_n[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
if even_count == n or odd_count == n:
    print(*arr_n)
else:
    arr_n.sort()
    print(*arr_n)


# for i in range(1, n):
#     odd = arr_n[i] + arr_n[i - 1]
#     if odd % 2 != 0:
#         if arr_n[i] < arr_n[i - 1]:
#             output.append(arr_n[i])
#             output.append(arr_n[i - 1])
#     else:
#         output.append(arr_n[i - 1])
#         output.append(arr_n[i])

# print(*output)
