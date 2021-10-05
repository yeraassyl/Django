if __name__ == '__main__':

    n = int(input())
    arr = [int(x) for x in input().split()]
    max_ = max(arr)

    for i in sorted(arr)[::-1]:
        if i != max_:
            print(i)
            break
