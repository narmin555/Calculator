def sum(a,b):
  return a+b

def deduction(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b


print("Hello my friend,welcome to our calculator.")

print("Which operation do you want?")

print("1.Sum")
print("2.Deduction")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

while True:
  select=int(input("Your operation: "))
  if select in (1,2,3,4):
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    if select==1:
      print("{} + {} = {}".format(num1,num2,sum(num1,num2)))
    elif select==2:
      print("{} - {} = {}".format(num1,num2,deduction(num1,num2)))
    elif select==3:
      print("{} * {} = {}".format(num1,num2,multiply(num1,num2)))
    elif select==4:
      print("{} / {} = {}".format(num1,num2,divide(num1,num2)))
  elif select==5:
    print("Exiting...")
    break        
  else:
    print("Invalid command")
    break

