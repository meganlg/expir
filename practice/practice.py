#######
#problemset1
def foo(n):
    if n%2==0 and n>20:
        print('Not Weird')
    elif  n%2==0 and (2<=n<=5):
        print('Not Weird')
    #elif range(6,20):
        #print('Weird')
    else:
        print('Weird')

foo(20)
foo(3)
foo(4)
foo(24)
foo(18)

#other example
def foo2(n):
    if n%2==0 and n>20:
        print('Not Weird')
    elif  n is even and n in range(2,5):
        print('Not Weird')
    elif n in range(6,20):
        print('Weird')
    else:
        print('Weird')

foo2(4)



############
#problemset2
def squares(n):
    for i in range(0,n):
        print(i**2)

squares(5)

    #other examples
def squares2(n):
    [print(i**2) for i in range(n)]

def squares3(n):
    for i in range(0, n):
        print(i * i)

def squares4(n):
    for i in range(n):
	       print(i*i)


############
#problemset3
