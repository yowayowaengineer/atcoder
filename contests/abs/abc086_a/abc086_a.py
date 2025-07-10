# https://atcoder.jp/contests/abs/tasks/abc086_a
a, b = map(int, input().split())
ans = "Even" if a * b % 2 == 0 else "Odd"
print(ans)