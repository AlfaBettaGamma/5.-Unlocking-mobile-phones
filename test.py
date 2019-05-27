def  SynchronizingTables(N, ids, salary):
  new_ids = []
  new_salary = []
  fin_salary = []
  if len(ids) == len(salary) and len(ids) == N:
    for i in range(N):
      new_ids.append(ids[i])
      new_salary.append(salary[i])
    for i in range(N - 1):
      for j in range(N - i - 1):
        if new_ids[j] > new_ids[j + 1] :
          new_ids[j], new_ids[j + 1] = new_ids[j + 1], new_ids[j]
        if new_salary[j] > new_salary[j + 1] :
          new_salary[j],new_salary[j + 1] = new_salary[j + 1], new_salary[j]
    for i in range(N):
      for j in range(N):
        if ids[i] == new_ids[j] :
          fin_salary.append(new_salary[j])
    return fin_salary, new_ids
  else:
    return print("Неверное значение!")
print(SynchronizingTables(3,[50,1,1024],[20,100,90]))
  

def test1():
  SynchronizingTables(3,[50,1,1024],[20000,100000,90000])

def test2():
  SynchronizingTables(2,[50,1,1024],[20000,100000,90000])

def test3():
  SynchronizingTables(3,[50,1,1024],[20000,100000,90000,2000])

