#  == Q:21-Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M ==


def construct(num, m, a):
  ind = 0

  for i in range(num):
    if (a[i]!=-1):
      ind = i
      break

  for i in range(ind-1, -1, -1):
    if (a[i]==-1):
      a[i]=(a[i + 1]-1 + m)% m

  for i in range(ind + 1, num):
    if(a[i]==-1):
      a[i]=(a[i-1]+1)% m
  print(*a)

num, m = 6, 7
a =[5, -1, -1, 1, 2, 3]
construct(num, m, a)
