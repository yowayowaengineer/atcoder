# https://atcoder.jp/contests/abc415/tasks/abc415_b

S = input()
work = ""
for i in range(len(S)):
    char = S[i]
    if (char == "#"):
        if (len(work) == 0):
            work = str(i+1) + ","
        else:
            print(work + str(i+1))
            work = ""