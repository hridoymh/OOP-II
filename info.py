"""Name: MD. Mehedi Hasan
   ID: 191-15-2395
"""

class info:
  def __init__(self):
    self.name = input('Enter your Name: ')
    self.id = input('Enter your ID: ')
    self.dpt = input('Enter your Department: ')
    self.email = input('Enter your Email: ')
    
  def echo(self):
    print('*******Your info************')
    print('Your Name is ',self.name,'')
    print('Your ID is ',self.id,'')
    print('Your Department is ',self.dpt,'')
    print('Your Email is ',self.email,'')
    

my = info()
my.echo()
