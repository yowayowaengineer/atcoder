# https://atcoder.jp/contests/abs/tasks/abc083_b
N, A, B = input().split()
n = int(N)
a = int(A)
b = int(B)

ans = 0
for i in range(n+1):
    sum = 0
    for char in str(i):
        sum += int(char)
    if (a <= sum & sum <= b):
        ans += i 

print(ans)