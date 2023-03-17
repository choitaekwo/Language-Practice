# list type
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))   # 1

subway.append("하하")       # 맨 뒤에 추가
print(subway)

subway.insert(1, "정형돈")   # 원하는 위치에 추가
print(subway)

print(subway.pop())     # 맨 뒤에서부터 꺼냄
print(subway)
print(subway.pop())     
print(subway)
print(subway.pop())     
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))    # 몇 개 있는지

num_list = [5, 2, 4, 3, 1]    # 정렬
num_list.sort()
print(num_list)

num_list.reverse()    # 거꾸로 정렬
print(num_list)

num_list.clear()    # 모두 지우기
print(num_list)

mix_list = ["조세호", 20, True]  # 다양한 자료형 함께 사용
print(mix_list)

num_list = [5, 2, 4, 3, 1] 
num_list.extend(mix_list)      # 리스트 확장
print(num_list)


# 딕셔너리 (key : value)
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)   # True
print(5 in cabinet)   # False

cabinet["A-3"] = "김종국"    # 추가
print(cabinet)
del cabinet["A-3"]          # 삭제
print(cabinet)

print(cabinet.keys())    # 키만 출력
print(cabinet.values())  # value만 출력
print(cabinet.items())   # 쌍으로 출력

cabinet.clear()          # 모두 지우기
print(cabinet)


# 투플 (tuple)
menu = ("등심", "안심")
print(menu[0])
print(menu[1])

name = "김종국"
age = 40
hobby = "코딩"
print(name, age, hobby)

(name, hobby, age) = ("김종국", "코딩", 20)
print(name, hobby, age)


# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

# 합집합 (java를 할 수 있거나 python을 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남 (값 추가)
python.add("김태호")
print(python)

# java를 까먹음 (값 삭제)
java.remove("김태호")
print(java)


# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


# (quiz)
USERS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
from random import*
shuffle(USERS)
print(f"치킨 당첨자 : {sample(USERS, 1)}")
shuffle(USERS)
print(f"커피 당첨자 : {sample(USERS, 3)}")

print("---- 축하합니다 ----")

# 방법 2
ID = range(1,21)    # type이 리스트가 아님
ID = list(ID)       # 리스토로 변경
shuffle(ID)
winners = sample(ID, 4)
print(f"치킨 당첨자 : {winners[0]}")
print("커피 당첨자 : {0}".format(winners[1:]))

print("---- 축하합니다 ----")



