if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(set(arr))
    a.sort()
    a.reverse()
    print(a[1])
