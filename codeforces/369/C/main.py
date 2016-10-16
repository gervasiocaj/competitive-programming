n = int(input())
q = []
p = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, t = [int(i) for i in input().split()]
    p[a].append(b)
    p[b].append(a)
    if t == 2: q.append((a, b))

if len(q) == 0:
    print(0)
else:
    r = [1]
    t = [0] * (n + 1)
    while len(r) > 0:
        a = r.pop()
        for b in p[a]:
            t[b] = a
            if len(p[b]) > 1:
                p[b].remove(a)
                r.append(b)
    s = [0] * (n + 1)
    for a, b in q:
        if t[a] == b:
            s[a] = 1
        else:
            s[b] = 1
    s[1] = 2
    for a in range(1, n + 1):
        if s[a] == 1:
            a = t[a]
            while s[a] != 2:
                s[a]= 2
                a = t[a]
    s = [i for i, j in enumerate(s) if j == 1]
    print(len(s))
    print(' '.join([str(i) for i in s]))
