# https://atcoder.jp/contests/abs/tasks/abc081_b
N = int(input())
A = list(map(int, input().split()))
ans = 0
while True:
    if (all(a % 2 == 0 for a in A)):
        ans += 1
        A = [a // 2 for a in A]
    else:
        break
print(ans)

# ↓↓↓ Before

# def is_all_even(array):
#     is_even = True
#     for a in array:
#         if a % 2 != 0:
#             is_even = False
#     return is_even
# def make_new_list(array):
#     new_list = []
#     for a in array:
#         new_list.append(a / 2)
#     return new_list
# def count_even_list(array, count):
#     if (is_all_even(array)):
#         count += 1
#         count_even_list(make_new_list(array), count)
#     else:
#         print(count)
# count_even_list(A, 0)


