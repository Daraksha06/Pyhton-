def add(func):
    def wrapper(*a):
        func(*a)
        sum=0
        for i in a:
            sum+=i
        print(f"sum of {a} is {sum}")
    return wrapper
def mul(func):
    def wrapper(*a):
        func(*a)
        pro=1
        for i in a:
            pro*=i
        print(f"mul of {a} is {pro}")
    return wrapper
@mul
def calc(a,b):
    pass
calc(5,10)


