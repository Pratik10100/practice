len=input()
s=input()
i=0
while i<len:
	x=s[i]
	count=0
	j=i
	while j<len:
		if s[j]==x:
			count=count+1
			s[j]=-1
		j=j+1
	su=x+' '
	su=su+count
	print su
	i=i+1
