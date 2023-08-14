




def s():
    sl = list(map(int , input().split() ))

    n = len(sl)
    for i in range(n-1):
        min_index = i


        for j in range(i+1, n):
            if sl[j] < sl[min_index]:
                min_index = j
        if min_index != i:
            sl[i], sl[min_index] = sl[min_index], sl[i]
    return sl


if __name__ == '__main__':
    print(s())