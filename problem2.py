import math

def fib(n):
 a,b = 1,1
 c = 0
# print 0
# print 1
 while(b<n):
  a,b = b,a+b
  if (a%2==0):
    c+=a
  print a
 print c
 return
fib(4000000)

  
