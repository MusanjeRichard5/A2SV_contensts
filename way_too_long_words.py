"""
Solution
read input first n = number of words
loop where range is n
in the loop read input of every word
count the length of each word as sz
if sz is less than or equal to 10
print the word
else
subtract 2 from sz as diff
then construct output with word[0] and word[sz] with diff in middle
print the output
"""

n = int(input())

for _ in range(n):
    word = input()
    sz = len(word)
    if sz <= 10:
        print(word)
    else:
        diff = sz - 2
        output = word[0] + str(diff) + word[sz - 1]
        print(output)
