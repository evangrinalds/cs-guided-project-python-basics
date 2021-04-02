def fibonacciSimpleSum2(n):
  fibs = {}
  for i in range(n):
    if i == 0 or i == 1: 
      fibs[i] = 1
      if n - fibs[i] in fibs.values():
        return True
    elif fibs[i-1] + fibs[i-2] > n: 
      break
    else:
      fibs[i] = fibs[i-1] + fibs[i-2]
      if n - fibs[i] in fibs.values():
        return True
  if n in fibs.values(): 
    return True 
  return False
  print(fibs)
