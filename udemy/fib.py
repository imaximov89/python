def fib(num):
    a = 0
    b = 1
    for i in range(num):
        temp = a
        a = b
        b = temp + b
        yield a

        
for x in fib(10):
    print(x)