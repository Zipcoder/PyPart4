def fibonacci_linear(n):
  v1 = 0
  v2 = 1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    arr1 = [0, 1]

    while len(arr1) !=n:
      arr1.append(arr1[len(arr1)-2] + arr1[len(arr1)-1])
  return arr1[len(arr1)-2] + arr1[len(arr1)-1]

print(fibonacci_linear(10))
