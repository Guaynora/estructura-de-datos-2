import random
def unico(x,L):
  esUnico=True
  for i in range(len(L)):
    if x==L[i]:
      esUnico=False
      break
  return esUnico
L=[]
j=0
while j<10:
  x=random.randint(80,99)
  if unico(x,L):
    L.append(x)
    j+=1
print(L)
L.sort()
print(L)
