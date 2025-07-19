# https://atcoder.jp/contests/abc415/tasks/abc415_d

N, M = map(int, input().split())

ans = 0
i = N
e = 0

for j in range(M):
    A, B = map(int, input().split())
    while (i >= A or e >= A):
        print("#" + str(i) + "," + str(e))
        if (e >= A):
            e -= A
            i += B
            ans += 1
        else:
            e += i
            i = 0

print(ans)