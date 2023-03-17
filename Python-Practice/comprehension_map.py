# comprehension
result = [i for i in range(1,6)] # 리스트
print(result)

li2 = {"1번": 1, "2번" : 2, "3번" : 3, "4번" : 4, "5번" : 5}
result2 = {key:val for key,val in li2.items()}  # 딕셔너리
print(result2)

result3 = (i*i for i in range(1,6))  # 집합(set)
print(result3)   # generator (for문으로 값을 사용 가능)
for value in result3:  # 값을 기억하지 않음. 한 번만 불러올 수 있음
    print(value)


# map함수
def plus(x,y):
    return x+y

z = map(plus, ("1번 : ", "2번 : ", "3번 : "), ("1", "2", "3"))
z = list(z)   # list로 변환해야 값을 볼 수 있음
print(z)

def mul(a, b):
    return a*b

c = map(mul, [1, 2, 3], [1, 2, 3])
print(list(c))

# lambda 함수 이용
tmp = map(lambda num1,num2 : num1 / num2, (9, 6, 3), (3, 2, 1))
print(list(tmp))

