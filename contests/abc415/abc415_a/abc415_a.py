# https://atcoder.jp/contests/abc415/tasks/abc415_a
N = int(input())
A = list(map(int, input().split()))
X = int(input())

ans = "No"
for a in A:
    if (a == X):
        ans = "Yes"
        break

print(ans)