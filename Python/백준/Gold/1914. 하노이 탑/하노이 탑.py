def h(n,k):
	if n==0:
		return k
	return h(n-1,k*2+1)
def m(n,s,t,e):
	if n==1:
		print(s,t)
	else:
		m(n-1,s,e,t)
		print(s,t)
		m(n-1,e,t,s)
n=int(input())
print(h(n,0))
if n<=20:
	m(n,1,3,2)