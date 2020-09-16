#Google Get Ahead + Interview Practice 2 (Matching Parentheses)
#Group 3: Python with Mitch McDermott

base = input()
target = input()

def isPart(subString):
    return subString in base

if __name__ == "__main__":
    num = 0
    if isPart(target) == False:
        i = 1
        while isPart(target[i:]) == False or isPart(target[:i]) == False:
            i += 1
            if i > len(target):
                i = len(base)
                break
        num = i
    print(num)