from random import*

# 용어 정리
# 클래스 : 제품의 설계도
# 객체 : 설계도로 만든 제품
# 속성 : 클래스 안의 변수
# 메서드 : 클래스 안의 함수
# 인스턴스 : 메모리에 살아있는 객체 (객체와 같다고 생각하면 됨)


# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다".format(name))
        
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 공격 유닛
class AttackUnit(Unit):  # Unit의 멤버변수 상속
    def __init__(self, name, hp, speed, damage):  
        Unit.__init__(self, name, hp, speed)   # 상속
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))
        
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
        
# 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".foramt(self.name))
            
# 탱크
class Tank(AttackUnit):
    # 시즈모드
    seize_developed = False # 시즈모드 개발여부
    
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
        
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
    
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):   # 다중상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)   # 지상 speed 0
        Flyable.__init__(self, flying_speed)
        
    def move(self, location):     # move() 재정의
        self.fly(self.name, location)
        
# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 (해제 상태)
        
    def clocking(self):
        if self.clocked == True:  # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다".format(self.name))
            self.clocked = False
        else:  # 클로킹 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다".format(self.name))
            self.clocked = True
            
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def gmae_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
    

# 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")
    
# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
        
# 전군 공격
for unit in attack_units:
    unit.attack("1시")
    
# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))  # 공격은 랜덤으로 받음(5~20)
    
# 게임 종료
gmae_over()


# quiz (부동산)
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,\
            self.price, self.completion_year)
        
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()




class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital
        
    def show(self):
        print(f"국가 : {self.name}  수도 : {self.capital}")
        
class Korea(Country):
     def __init__(self, name, capital, population, continent):    # 생성자도 오버라이딩
        self.name = name
        self.capital = capital
        self.population = population
        self.continent = continent
      
     def show(self):
         super().show()   # 부모 클래스의 show() 호출
         print(f"국가 : {self.name}  수도 : {self.capital}   인구 : {self.population}  대륙 : {self.continent}")   # show() 재정의 
         
# a = Korea("대한민국", "서울", "5000만", "아시아")
# a.show()
        
class Enemy:
     def __init__(self, enemy_name, enemy_capital):
        self.enemy_name = enemy_name
        self.enemy_capital = enemy_capital
        
     def show_enemy(self):
        print(f"국가 : {self.enemy_name}  수도 : {self.enemy_capital}")

class World(Korea, Enemy):   # 다중상속
    def __init__(self, name, capital, population, continent, enemy_name, enemy_capital):
        Korea.__init__(self, name, capital, population, continent)
        Enemy.__init__(self, enemy_name, enemy_capital)
        
    def reconcile(self):
        print(f"{self.name} 과 {self.enemy_name}  화해하시길 바랍니다")
        
c = World("대한민국", "서울", "5000만", "아시아", "북한", "평양")
c.show()
c.show_enemy()
c.reconcile()


# private 멤버 변수
class TestClass:
    def __init__(self, a, b, c):
        self.a = a
        self.__b = b
        self.c = c
        
    def sum3Num(self):
        return self.a + self.__b + self.c
    
obj1 = TestClass(10, 30, 70)
print(f"세 수의 합 : {obj1.sum3Num()}")
print(f"obj1.a = {obj1.a}  obj1.c = {obj1.c}")
print(f"obj1.__b = {obj1.__b}")   # 객체를 사용해서 private 멤버 접근 불가
