n = int(input())


for _ in range(n):
    arr_list = list(map(int, input().split()))
    arr_list.sort()
    if (arr_list[0] + arr_list[1]) == arr_list[2]:
        print("YES")
    else:
        print("NO")
