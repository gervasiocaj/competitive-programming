n = int(input())
x = [int(i) for i in input().split()]
y = [x[i]-1 for i in range(n)]

q = [0]
i = 0
res = [-1] * n
res[0] = 0

while i < len(q):
    c = q[i]
    i+=1
    if c > 0 and res[c-1] == -1:
        res[c-1] = res[c] + 1
        q.append(c-1)
    if c < n-1 and res[c+1] ==- 1:
        res[c+1] = res[c] + 1
        q.append(c+1)
    if res[y[c]] == -1:
        res[y[c]] = res[c] + 1
        q.append(y[c])

print(' '.join([str(i) for i in res]))
