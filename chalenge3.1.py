def search(list,n):
  for i in range(len(list)):
    if list[i] == n:
      return True
    else:
      return False
list = [1,2,'sachin',4,'geeks',6] 
n = 'geeks'
if search(list, n):
  print("found")
else:
  print("not found")