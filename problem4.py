def isPalindrome(n):
    s = str(n)
    m = len(s)
#    print m
    p = True
    for i in range(0, m//2):
#      print 'i(' + str(i) + '): ' + str(s[i]) + '\t' + str(s[m-i-1])
      if (s[i]!=s[m-i-1]):
        p = False
    return p
#print isPalindrome(9009)

c = 0
cx = 0
cy = 0
for x in range (999,1,-1):
  for y in range (999,1,-1):
    if (isPalindrome(x*y)):
      if (x*y>c):
        c = x*y
        cx = x
        cy = y
        
print cx, cy, c