#classmethod
class Person:
    @classmethod
    def demo(cls):
        return "hello"
Person.demo()

def demo():
    return "hello"

asd=demo
asd()
del demo
asd()
type(asd)
asd
a=12
b=12




def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")
func_needs_decorator()
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()


    