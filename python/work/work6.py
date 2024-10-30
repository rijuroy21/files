while(True):
    op=int(input('''
                1.Add
                2.Substract
                3.Multiply
                4.division
                5.exit
                enter your choice:'''))
    if op==1:
        def add():
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=a+b
            return c
        add=add()
        print(add)
    elif op==2:
        def sub():
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=a-b
            return c
        sub=sub()
        print(sub)
    elif op==3:
        def mul():
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=a*b
            return c
        mul=mul()
        print(mul)
    elif op==4:
        def div():
            a=int(input("enter first number:"))
            b=int(input("enter second number:"))
            c=a/b
            return c
        div=div()
        print(div)
    elif op==5:
        break  