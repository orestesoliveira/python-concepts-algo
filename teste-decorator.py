def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")

    return wrapper

@f1
def f():
    print("Hello F")

#f1(f)()
#with this we can decorate a function

#x = f1(f)
#x()

#instead of doing the following we can decorate tge f() with @f1
#f = f1(f)
f()

@f1
def g(a,b):
    print(a,b)

g(">>>>>>>>>>>>>>>>>>>>",77)



#and if i want to return values?

def f4(func):
    def wrapper(*args, **kwargs):
        print("------Started")
        retorno = func(*args, **kwargs)
        print("-------Ended")
        return retorno

    return wrapper

@f4
def add(x,y):
    return x + y


print(add(7,9))