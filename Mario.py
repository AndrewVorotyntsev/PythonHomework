def tower(h):
    print('height:',h)
    for i in range(1,h+1):
        print((h-i)*' '+(i+1)*"#",)


def check_height(h):
    if ((h>0) and (h<24)):
        tower(h)
    else:
        print('Wrong height,write height again')
        h=int(input())
        check_height(h)


def check_int(h):
    try:
        int(h)
        h=int(h)
        check_height(h)
    except ValueError:
        print('Wrong height,write height again')
        h=input()
        check_int(h)


print('Write height')
h=input()
check_int(h)
