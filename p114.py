# nums = list(range(1,10,2))
# print(nums)
# # print(type(nums))
# for i in range(2,11,2):
#     print(i)

# nums=(3,1,4,1,5,9,2)
# print(type(nums))
# for i in nums:
#     print(i)


def p(space,space_num, *args):
    str = ""
    for i in args:
        str = str+(space*space_num)+i
    print(str)
p(",",3,"👍","😊")
p(",",3,"👍","😊","😒","👌")