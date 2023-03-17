# 영화 가격 모듈
import package_practice.theater_module as theater_module
theater_module.price(3)    # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4)  # 4명이서 조조할인 가격
theater_module.price_soldier(5)  # 5명 군인 가격

import package_practice.theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from package_practice.theater_module import*
price(3)
price_morning(4)
price_soldier(5)

from package_practice.theater_module import price, price_morning  
price(3)
price_morning(4)

from package_practice.theater_module import price_soldier as price
price(5)            # price_soldier를 price라는 별명으로 사용하겠음
                    # 원래의 price 함수와는 다른 거임
                    
                    
# 여행 가격 모듈
import package_practice.thailand
trip_to = package_practice.thailand.ThailandPackage()
trip_to.detail()

from package_practice.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from package_practice import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from package_practice import *
trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()


# 모듈 위치
import inspect
import random
print(inspect.getfile(random))  # random 모듈 위치
print(inspect.getfile(thailand)) # thailand 모듈 위치

# 수강완료
import package_practice.byme
byme.sign()
