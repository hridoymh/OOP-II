"""Name: MD. Mehedi Hasan
   ID: 191-15-2395
"""

class student:
  av_mark = 0

  def __init__(self):
    self.id = input('Enter your ID:')
    print('Enter your marks')
    for i in range(0,3):
      self.av_mark += int(input())
    self.av_mark /= 3

  def echo(self):
    
    print('ID: ',self.id)
    print('Average',self.av_mark)




s_list = list()
n = 8


for i in range(0,n):
  print('Student ',i)
  s_list.insert(i,student())
  print()

for i in range(0,n):
  print('Student ',i)
  s_list[i].echo()
  print()
