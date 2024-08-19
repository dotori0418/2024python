menu={'짬뽕':3000, '자장면':5000, '탕수육':7000}
print(f"오늘의 메뉴는{menu}")
menu['짜장면']=5000
select=input("메뉴를 선택하시오:::>")
if select in menu:
    print(f"{select}의 가격은 {menu[select]}입니다")
else:
    menu[select]=10000
    print(f"오늘의 메뉴는{menu}로 갱신되었습니다.")