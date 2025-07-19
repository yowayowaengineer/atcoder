# https://atcoder.i1p/contests/abc415/tasi2s/abc415_c

T = int(input())
ansList = []
for i in range(T):
    N = int(input())
    S = input()

    ans = "No"
    nList = []
    for i1 in range(N):
        if (S[i1] == "1"):
            break
        for i2 in range(N):
            if (i2 != i1):
                if (S[i1+i2] == "1"):
                    break
                for i3 in range(N):
                    if (i3 != i2 and i3 != i1):
                        if (S[i1+i2+i3] == "1"):
                            break
                        for i4 in range(N):
                            if (i4 != i3 and i4 != i2 and i4 != i1):
                                if (S[i1+i2+i3+i4] == "1"):
                                    break
                                for i5 in range(N):
                                    if (i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1):
                                        if (S[i1+i2+i3+i4+i5] == "1"):
                                            break
                                        for i6 in range(N):
                                            if (i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1):
                                                if (S[i1+i2+i3+i4+i5+i6] == "1"):
                                                    break
                                                for i7 in range(N):
                                                    if (i7 != i6 and i7 != i5 and i7 != i4 and i7 != i3 and i7 != i2 and i7 != i1):
                                                        if (S[i1+i2+i3+i4+i5+i6+i7] == "1"):
                                                            break
                                                        for i8 in range(N):
                                                            if (i8 != i7 and i8 != i6 and i8 != i5 and i8 != i4 and i8 != i3 and i8 != i2 and i8 != i1):
                                                                if (S[i1+i2+i3+i4+i5+i6+i7+i8] == "1"):
                                                                    break
                                                                for i9 in range(N):
                                                                    if (i9 != i8 and i9 != i7 and i9 != i6 and i9 != i5 and i9 != i4 and i9 != i3 and i9 != i2 and i9 != i1):
                                                                        if (S[i1+i2+i3+i4+i5+i6+i7+i8+i9] == "1"):
                                                                            break
                                                                        for i10 in range(N):
                                                                            if (i10 != i9 and i10 != i8 and i10 != i7 and i10 != i6 and i10 != i5 and i10 != i4 and i10 != i3 and i10 != i2 and i10 != i1):
                                                                                if (S[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10] == "1"):
                                                                                    break
                                                                                for i11 in range(N):
                                                                                    if (i11 != i10 and i11 != i9 and i11 != i8 and i11 != i7 and i11 != i6 and i11 != i5 and i11 != i4 and i11 != i3 and i11 != i2 and i11 != i1):
                                                                                        if (S[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11] == "1"):
                                                                                            break
                                                                                        for i12 in range(N):
                                                                                            if (i12 != i11 and i12 != i10 and i12 != i9 and i12 != i8 and i12 != i7 and i12 != i6 and i12 != i5 and i12 != i4 and i12 != i3 and i12 != i2 and i12 != i1):
                                                                                                if (S[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12] == "1"):
                                                                                                    break
                                                                                                for i13 in range(N):
                                                                                                    if (i13 != i12 and i13 != i11 and i13 != i10 and i13 != i9 and i13 != i8 and i13 != i7 and i13 != i6 and i13 != i5 and i13 != i4 and i13 != i3 and i13 != i2 and i13 != i1):
                                                                                                        if (S[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13] == "1"):
                                                                                                            break
                                                                                                        for i14 in range(N):
                                                                                                            if (i14 != i13 and i14 != i12 and i14 != i11 and i14 != i10 and i14 != i9 and i14 != i8 and i14 != i7 and i14 != i6 and i14 != i5 and i14 != i4 and i14 != i3 and i14 != i2 and i14 != i1):
                                                                                                                if (S[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14] == "1"):
                                                                                                                    break
                                                                                                                for i15 in range(N):
                                                                                                                    if (i15 != i14 and i15 != i13 and i15 != i12 and i15 != i11 and i15 != i10 and i15 != i9 and i15 != i8 and i15 != i7 and i15 != i6 and i15 != i5 and i15 != i4 and i15 != i3 and i15 != i2 and i15 != i1):
                                                                                                                        if (S[i1+i2+i3+i4+i5+i6+i7+i8+i9+i10+i11+i12+i13+i14+i15] == "1"):
                                                                                                                            break
                                                                                                                        ans = "Yes"
    ansList.append(ans)

for a in ansList:
    print(a)