def linear_recursion(n,exp):
  if exp==0:
    return 1
  elif exp%2==0:
    auxiliar=linear_recursion(n, exp//2)
    return auxiliar*auxiliar
  else:
    return base * linear_recursion(n, exp-1)

base=2
exp=10124
ans=linear_recursion(base,exp)
print(ans)
