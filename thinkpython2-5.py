# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A-0i1UIj7TX6h4HoRZWdmRNtd5tqgPmA
"""

# 5.1
import time

s = int(time.time())

m = s // 60
cs = s % 60

h = m // 60
cm = m % 60

d = h // 24
ch = h % 24

y = d // 365
cd = d % 365

year = 1970 + y


print(s, m ,h, d, year)
print("{}day {}hour {}min {}sec".format(cd, ch, cm ,cs))

#5.2

def check_fermat(a, b, c, n):
  if n > 2:
    if (a ** n) + (b ** n) == (c**n):
      print("Holy smokes, Fermat was wrong")
    else:
      print("No, that doesn't work")
  else:
    print("No, that doesn't work")
    
check_fermat(1,2,3,2)

#5.3-1
import time

def is_triangle(a, b, c):
  list_a = [a, b, c]
  long_s= max(list_a)
  list_a.remove(long_s)
  mid_s = max(list_a)
  list_a.remove(mid_s)
  short_s = list_a[0]
  if short_s + mid_s > long_s:
    print("Yes")
  else:
    print("No")
    
    
time1 = time.time()  
is_triangle(4, 5, 3)
time2 = time.time()

print(time2-time1)

#5.3-2

def check_tri():
  a = int(input("First num: "))
  b = int(input("Second num: "))
  c = int(input("Third num: "))
  list_a = [a, b, c]
  is_triangle(list_a)
  
def is_triangle(list_a):
  long_s= max(list_a)
  list_a.remove(long_s)
  mid_s = max(list_a)
  list_a.remove(mid_s)
  short_s = list_a[0]
  if short_s + mid_s > long_s:
    print("Yes")
  else:
    print("No")
    
check_tri()

#5.4-1 : If run function recurse(-1,0), the function will run infinitly.

#5.4-2
def recurse(n, s):   
  if n > 0:
    if n == 0:
      print(s)
    else:
      recurse(n-1, n +s)
  else:
    print("Wrong input number")
    
recurse(3,0)

