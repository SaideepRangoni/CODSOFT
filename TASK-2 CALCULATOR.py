num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
operator=input("enter the operator:")
if (operator=='+'):
  print("answer=",num1+num2)
elif(operator=='-'):
  print("answer=",num1-num2)
elif(operator=='*'):
  print("answer=",num1*num2)
elif(operator=='%'):
  print("answer=",num1%num2)
elif(operator=='/'):
  print("answer=",num1/num2)
elif(operator=='**'):
  print('answer=',num1**num2)
else:
  print("enter valid operator")
  