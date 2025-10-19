# variable scope = where a variable is visible and acessible
# scope resolution = (LEGB) local > encolsed > global > Build-in 


def func1():
    a = 1
    print(a)

func1()
# var inside funcs are local


def func2():
    x = 1
    def func3():
    func3()

func2()

# var enclosed in func 2 but can be called by func3

def func4():
    print(x)

def func5():
    print(x)

x = 3

func4()
func5()

# var global has been defined outside of the func

from math import e

def func6()
    print(e)

func6()

# var built int 