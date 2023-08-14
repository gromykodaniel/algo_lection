def s():

    skobki = input()

    stack = []
    ans = True

    approve = [ ('(',')') ,  ('{','}') , ('[',']') ]
    for i in skobki:

        if i in '({[':
            stack.append(i)

        elif i in ')}]' :
            if len(stack ) == 0:
                ans = False
                break
            a = stack.pop()

            combo = (a,i)
            if combo in approve :
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
