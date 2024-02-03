# Variable(Global & Local) & Input/Output Function

# Normal output
print('Python Playground');

# Output using variable
name = 'Md Asaduzzaman'
print('My name is: ',name)

age = 22
print('My age is : ',age)


# Global variable vs local variable
number1 = 100

# Work global variable
def function1():
    print('Global Variable is: ',number1)
function1()

# Work local variable
def function2():
    number1 = 200
    print('Local variable is: ',number1)
function2()