def s():

    skobki = input()

    stack = []
    ans = True

    #approve = [ ('(',')') ,  ('{','}') , ('[',']') ]

    mapa = {'(':')' , '[':']' , '{':'}'}
    for i in skobki:

        if i in mapa.keys():


            stack.append(i)

        elif i in mapa.values() :
            if len(stack ) == 0:
                ans = False
                break
            a = stack.pop()


            if mapa[a] and mapa[a] == i:
                continue
            # if a == '(' and i == ')':
            #     continue
            # if a == '{' and i == '}':
            #     continue
            # if a == '[' and i == ']':
            #     continue

            ans = False
            break

    if stack: ans = False
    return ans
if __name__ == '__main__':
    print(s())
