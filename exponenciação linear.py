def linear(a,b):
  if a == 0:
    return 1
  else:
    return b * linear(a-1, b)

base=2
expoente=12345533
ans=linear(base,expoente)

print(ans)
