

def s():
    sl = list(map(int , input().split() ))

    n = len(sl)

    for i in range( 1 , n):

        l = i - 1
        now = sl[i]
        while l != 0:

            if now <= sl[l]:

                sl[l+1] , sl[l] = sl[l] , now
                l -= 1
            else:
                break
    return sl


if __name__ == '__main__':
    print(s())