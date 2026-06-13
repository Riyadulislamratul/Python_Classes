
# Function Syntax
# def function_name():
#     statement
# ----------- Parameter------
# def greet():
#     print("Hello World!")

# greet()

# ------------ Arguments----------
# def greet(name):
#     print("Hello" , name)

# greet("Udoy")

# Here name is a parameter and "Udoy" is an argument.


# def sum(x, y):
#     print(x+y)
# sum(25, 50)

# def multi(a, b):
#     print(a*b)
# multi(502, 60)

# ------------- With Return Statement-----------

# def square(x):
#     print(x*x)   
# result = square(7)
# print(result)  

# # Global Variable
# a = 30

# def square(x):
#     b=5  # Local Variable
#     return x*x
# result = square(7)
# print(result)  



# --------*Args---------

# def function_name(*args):
#     statement

# def show(*args):
#     print(args)
# show(1, 225, 30, 6, 5)



# def total(*num):
#     print(sum(num))
# total(52,45,548,549,41,654,5496,6)
# total(2,3)
# total(65465,68468474)




# ---------------**Kwargs----------
# def function_name(**kwargs):
#     statement


# def show(**kwargs):
#     print(kwargs)

# show(name = "jobaydul",
#      age = "21",
#      department = "CSE",
#      maraital_Status = "Married",
#      nationality = "Bangladeshi"
# )


# ----------------- Lambda Function-----------------------------

# lambda agruments: expression 

# square = lambda x: x*x

# print(square(7))



# large = lambda a, b: a if a>b else b

# print(large(35, 21))



# -----------------------------------Global varible ------------------------------------------

a = 55
b = 100

# -----------------------------------Local varible ------------------------------------------
def local_variable():
  
    print(b,a)


local_variable()


def global_varible():
    print(a,b)

global_varible()