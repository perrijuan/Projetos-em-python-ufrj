#codigo não otimizado para n >30
#fibonacci recursiva....
def fibonacci(n):
  if n<=1:
    return n
  else:
      return fibonacci(n-1)+fibonacci(n-2)

n = 38
print(fibonacci(n))
