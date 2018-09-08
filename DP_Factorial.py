"""
Author:
Bhaskar Gautam,
Data Mining Lab,
Indian Institute of Technology, Roorkee
"""

T = int(raw_input())
nmL = []
for i in range(T):
    nmL.append(int(raw_input()))

cache = {}
for i in range(2,100000):
    cache[i] = -1
cache[0] = 1
cache[1] = 1

def fact(n):
    # Memoization
    if n < 1:
        return 1
    CK = cache.keys()

    if n-1 in CK:
        # print("FOUND: n-1,cache",n-1,cache)
        cache[n] = (n*cache[n-1])%(10000000000007)
        return cache[n]
    else:
        # print("NOT FOUND: n-1,cache",n-1,cache)
        j = max(CK)
        while j != n and j not in CK:
            # print("j",j)
            cache[j] = (j*cache[j-1])%(1000000007)
            j = j + 1
            # print("Entered: j,cache",j,cache)
        # print("Entry via RECC: n,cache",n,cache)
        cache[n] = (n*fact(n-1))%(1000000007)
        return cache[n]

def DP_F(n):
    global cache
    if n == 0 or n == 1 :
        return cache[0];
    if cache[n] != -1:
        return cache[n]
    cache[n] = (n*DP_F(n-1))%(1000000007);
    return cache[n];

for i in range(T):
    tmp = i
    # print fact(nmL[i]) # Memoization of DP
    print DP_F(nmL[i])#%(1000000007) # DP
