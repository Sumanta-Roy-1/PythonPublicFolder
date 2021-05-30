
# *args and **kwargs
# *vars and **kvars - 
# import is * not the name

# def function_1(name, age, rollno):
#     print("the name of the student is ", name, "and age ", age, "and rollno is ", rollno)


def function_1(*args):
    print(type(args))
    if(len(args) ==3):
        print("the name of the student is ", args[0], "and age ", args[1], "and rollno is ", args[2])
    else:
        print("the name of the student is ", args[0], "and age ", args[1])

def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
      
function_1("Sumanta", 40)
function_1("Sumanta", 40, 3455)

print("**kwargs ......")
marklist = {"Sumanta" : 90,"Shiben": 100, "Pratima": 91, "Mina": 95}
printmarks(**marklist)