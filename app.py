def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  if a>b:
    return a/b
  else:
    return b/a

print(" 1. add,
      2. sub,
      3. multiply,
      4. divide")

choice=input("Enter your choice")

num1=float(input("enter 1st num')
num2=float(input("enter 1st num')

if choice=='1':
  print(add(num1, num2))

elif choice=='2':
  print(sub(num1, num2))

elif choice=='3':
  print(mul(num1, num2))

elif choice=='4':
  print(div(num1, num2))

else:
  print("Invalid")
