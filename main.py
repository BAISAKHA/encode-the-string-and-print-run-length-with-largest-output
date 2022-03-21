n=input()
l=[]
flag=""
for i in range (len(n)):
  m=0
  if (n[i]) in flag:
    continue
  for j in range(len(n)):
    if (j==i):
      continue
    elif (n[j]==n[i]):
      m+=1
  flag+=n[i]
  l.append(n[i])
  if (m==0):
    l.append(1)
  else:
    l.append(m+1)

print(l)
  

      
      
    
  