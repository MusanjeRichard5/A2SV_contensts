# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phone_book = {}
search_list = []

for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

while True:
    try:
        search_name = input()
        if search_name in phone_book:
            print(f"{search_name}={phone_book[search_name]}")
        else:
            print("Not found")
    except EOFError:
        break
