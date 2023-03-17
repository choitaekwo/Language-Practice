print(abs(-5))   # 절댓값
print(pow(4, 2)) # 제곱
print(min(1, 3, 5))
print(max(1, 3, 5))
print(round(3.14)) # 반올림
print(round(3.99))

# import math
# print(math.floor(9.99)) # 내림

from math import *
print(floor(9.99)) # 내림
print(ceil(9.99))  # 올림
print(sqrt(9))     # 제곱근 square root

# from math import floor
# print(floor(9.99)) # 내림

from random import *
print(random())    # 0.0 ~ 1.0 미만
print(random() * 10)  # 0.0 ~ 10.0 미만
print(int(random() * 10))  # 0 ~ 10 미만
print(int(random() * 10) + 1)  # 1 ~ 10 이하
print(int(random() * 45) + 1)  # 1 ~ 45 이하  

print(randrange(1, 46))    # 1 ~ 46 미만
print(randrange(1, 11, 3)) # 1부터 3씩 더한 수 중 하나
print(randint(1, 45))      # 1 ~ 45 이하

date = (randint(1, 30))
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다")
