n, m = [int(i) for i in input().split()]
res = 0

while n < m:
	res += 1
	if m % 2 == 0:
		m //= 2
	else:
		m += 1

res += n
res -= m

print(res)