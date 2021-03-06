

#7.1

import math


def mysqrt(a):
  x = 10
  while True:
    y = (x + a/x) / 2
    if y == x:
      break
    x = y
  return x



def test_square_root():
  print("a   mysqrt(a)           math.sqrt(a)       diff")
  print("-   ---------           ------------       ----")
  for a in range(1, 10):
    if a == 1 or a == 4 or a == 9:
      print(float(a), end = " ")
      print(mysqrt(a), end = "                 ")
      print(math.sqrt(a), end = "                ")
      print(math.sqrt(a) - mysqrt(a))
    else:
      print(float(a), end = " ")
      print(round(mysqrt(a), 14), end = "    ")
      print(round(math.sqrt(a), 13), end = "    ")
      print(math.sqrt(a) - mysqrt(a))
  
      
  
    
  
test_square_root()

#7.2
def eval_loop():
  while True:
    line = input("> ")
    if line == 'done':
      break
    n = eval(line)
  print(n)
    
eval_loop()

#7.3

import math

def facto(n):
  if n == 0:
    return 1
  else:
    r = facto(n-1)
    res = n * r
  return res
  


def estimate_pi():
  k = 0
  result = 0
  i = 2 * math.sqrt(2) / 9801 
  while True:
    a = facto(4*k) * (1103 + 26390 * k) 
    b = (facto(k) ** 4) * (396 ** (4*k) )
    c = i * a / b
    result = result + c
    
    if abs(c) < 1e-15:
      break 
    k += 1
  return 1 / result

print(estimate_pi())
print(math.pi)

