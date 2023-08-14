def s():

    skobki = input()

    stack = []
    ans = True
    for i in skobki:

        if i in '({[':
            stack.append(i)

        elif i in ')}]' :
            if len(stack ) == 0:
                ans = False
                break
            a = stack.pop()

            if a == '(' and i == ')':
                continue
            if a == '{' and i == '}':
                continue
            if a == '[' and i == ']':
                continue

            ans = False
            break
    return ans
if __name__ == '__main__':
    print(s())
