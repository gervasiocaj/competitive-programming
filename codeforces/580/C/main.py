n, m = [int(i) for i in input().split()]
f = [0]
f.append([int(i) for i in input().split()])
z = [1,0] + [0]*n
p = [[] for i in range(n + 1)]
res = 0

for i in range(1, n):
    a, b = [int(i) for i in input().split()]
    p[a].append(b)
    p[b].append(a)

p[1] += [0]
r = [len(x) == 1 for x in p]
act = 1
s=[(1,0)]
while act:
    a, b = s.pop()
    z[a] = 1
    act -= 1

    if f[a]:
    	b+=1
    else:
    	b=0

    if b <= m:
	    if r[a]:
	    	res += 1
	    for x in p[a]:
	        if not z[x]:
		        s += [(x,b)]
		        act += 1
print(res)