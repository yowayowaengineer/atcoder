# https://atcoder.jp/contests/abs/tasks/abc087_b
A = int(input())
B = int(input())
C = int(input())
X = int(input())

def count50(c):
    n = 0
    by100 = c // 2
    n += by100
    by500 = c // 10
    n += by500

    n += count100(by100)
    return n

def count100(c):
    n = 0
    by500 = c // 5
    n += by500
    return n

ans = 0

# 50円何枚分か
by50 = X // 50

if (C >= by50):
    ans += 1
    ans += count50(by50)
    print(count50(by50))

else:
    less = X - 50 * C
    lessBy100 = less // 100

    if (less % 100 == 0):
        if (B >= lessBy100):
            ans += 1
            ans += count50(C)
            print(ans)
            ans += count100(lessBy100)

        else:
            less2 = less - 100 * B
            lessBy500 = less2 // 500

            if (less2 % 500 == 0 & A >= lessBy500):
                ans += count100(B)
                ans += 1
    

# 100円何枚分か
by100 = X // 100

if (X % 100 == 0 ):
    if (B >= by100):
        ans += 1
        ans += count100(by100)

    else:
        less = X - 100 * B
        lessBy500 = less // 500

        if (less % 500 == 0 & A >= lessBy500):
            ans += count100(B)
            ans += 1

# 500円何枚分か
by500 = X // 500

if (X % 500 == 0 & A >= by500):
    ans += 1

print(ans)

