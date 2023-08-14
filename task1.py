

def s():
    sl = list(map(int , input().split() ))

    for i in range(len(sl)):

        for j in range(len(sl)-i-1):

            if sl[j] >= sl[j+1]:

                sl[j] , sl[j+1] = sl[j+1] , sl[j]

    return sl



if __name__ == '__main__':
    print(s())