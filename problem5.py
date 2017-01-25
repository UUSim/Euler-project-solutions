from __future__ import division

def divsEven(n,x):
  a = n/x
  b = n//x
  return a==b
  
#print divsEven(1,2)
#print divsEven(2,2)

def findN(k):
  a = 2
  while (a<999999999):
    e = True
    for i in range (k,2,-1):
      if (not divsEven(a,i)):
        a+=2
        e = False
    if (e):
      return a
  return -1
  
print findN(20)

# outcome (n=20) was 232792560