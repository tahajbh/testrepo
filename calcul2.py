num1= float(input("Please enter the first number: "))
operation = input("please enter the operator: ")
num2= float(input("please enter the siecond number: "))

if operation == "+":
    print(num1+num2)
    
elif operation == "-":
    print(num1-num2)

elif operation == "/":
    print(num1/num2)

elif operation == "*":
    print(num1*num2)

else:
    print('wrong operation,please check')
