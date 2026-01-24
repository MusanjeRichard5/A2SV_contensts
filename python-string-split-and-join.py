def split_and_join(line):
    # write your code here
    str = line.split()
    return "-".join(str)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
