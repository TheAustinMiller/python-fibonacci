def fib(n):
  if n <= 1:
    return n
  else:
    return (fib(n-1) + fib(n-2))

nTimes = 10
for i in range(nTimes):
  print(fib(i))
