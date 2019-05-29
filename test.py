def PatternUnlock( N, hits):
  st = ' '
  s = 0
  pr = 0
  fst = 0
  spf = []
  fs = []
  p = 0
  if hits.count(0) == 0 and N == len(hits):
    for i in range(N-1):
      if (hits[i] == 1 and hits[i + 1] == 2 or
         hits[i] == 1 and hits[i + 1] == 9 or
         hits[i] == 1 and hits[i + 1] == 6 or
         hits[i] == 2 and hits[i + 1] == 1 or
         hits[i] == 2 and hits[i + 1] == 3 or
         hits[i] == 2 and hits[i + 1] == 8 or
         hits[i] == 2 and hits[i + 1] == 5 or
         hits[i] == 3 and hits[i + 1] == 2 or
         hits[i] == 3 and hits[i + 1] == 4 or
         hits[i] == 4 and hits[i + 1] == 3 or
         hits[i] == 4 and hits[i + 1] == 5 or
         hits[i] == 5 and hits[i + 1] == 4 or
         hits[i] == 5 and hits[i + 1] == 2 or
         hits[i] == 5 and hits[i + 1] == 6 or
         hits[i] == 6 and hits[i + 1] == 5 or
         hits[i] == 6 and hits[i + 1] == 1 or
         hits[i] == 7 and hits[i + 1] == 3 or
         hits[i] == 7 and hits[i + 1] == 8 or
         hits[i] == 8 and hits[i + 1] == 7 or
         hits[i] == 8 and hits[i + 1] == 2 or
         hits[i] == 8 and hits[i + 1] == 9 or
         hits[i] == 9 and hits[i + 1] == 1 or
         hits[i] == 9 and hits[i + 1] == 8):
        s += 1
      elif (hits[i] == 1 and hits[i + 1] == 5 or
           hits[i] == 1 and hits[i + 1] == 8 or
           hits[i] == 2 and hits[i + 1] == 6 or
           hits[i] == 2 and hits[i + 1] == 9 or
           hits[i] == 2 and hits[i + 1] == 4 or
           hits[i] == 2 and hits[i + 1] == 7 or
           hits[i] == 3 and hits[i + 1] == 5 or
           hits[i] == 3 and hits[i + 1] == 8 or
           hits[i] == 4 and hits[i + 1] == 2 or
           hits[i] == 5 and hits[i + 1] == 1 or
           hits[i] == 5 and hits[i + 1] == 3 or
           hits[i] == 6 and hits[i + 1] == 2 or
           hits[i] == 7 and hits[i + 1] == 2 or
           hits[i] == 8 and hits[i + 1] == 1 or
           hits[i] == 8 and hits[i + 1] == 3 or
           hits[i] == 9 and hits[i + 1] == 2):
        s += 1.41421
  else:
    return print('Неверно введены занчения в список!')
  s = s*100000
  pr = int(s)
  while pr is not 0:
    p = pr%10
    pr = pr//10
    spf.insert(0,p)
  for i in range(len(spf)):
    if(spf[i] != 0):
      fs.append(spf[i])
  p = 10**(len(fs)-1)
  for i in range(len(fs)):
    fst = fst + (fs[i]*p)
    p = p//10
  st = str(fst)
  return st

def test():
  print(PatternUnlock( 10, [1,2,3,4,5,6,2,7,8,9]))

