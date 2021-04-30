print("원딜(이즈리얼) 게임을 시작합니다. ")
print("리신이(HP100) 이니시를 건다 이쿠!! ")
print("스킬을 사용하여 카이팅 하세요")
print("1.신비한화살","2.정수의 흐름", "3.비전이동","4.정조준일격")
dict_skill ={"1": "신비한 화살!!", "2":"정수의 흐름!!","3":"비전이동!!","4":"정조준 일격!!"}
list_damage = [10,20,30,40]
def sum(skill,hp=100):
    left=hp-skill
    return left  
    print("남은 피는: ",left)

use = int(input("스킬을 선택하세요"))
if use == 1:
    print(dict_skill["1"])
    print("리신의 피가",list_damage[0]," 만큼 깎였다")  
     
elif use == 2:
    print(dict_skill["2"])
    print("리신의 피가",list_damage[1],"만큼 깎였다")
elif use == 3:
    print(dict_skill["3"])
    print("리신의 피가",list_damage[2],"만큼 깎였다")
elif use == 4:
    print(dict_skill["4"])
    print("리신의 피가",list_damage[3],"만큼 깎였다")
else:
    print("잘못 선택하셨습니다")