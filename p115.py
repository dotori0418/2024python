# def p(space,space_num, *args):
#     str = ""
#     for i in args:
#         str = str+(space*space_num)+i
#     print(str)

def star(letter,space,*args):
    str = ""
    for i in range(0,space):
        str = str +(letter*i)
    print(str)

star("😒",3)
# 아래는 쌤 코드 위는 내 코드
def star(space,*args):
    for i in args:
        print(space*i)

star("👌",1,2,3)
    