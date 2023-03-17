# if
weather = input("오늘 날씨 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필여 없어요")
    
temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0<= temp < 10:         # 이렇게도 됨 (and)
    print("외투를 챙기세요")
else:
    print("너무 추워요")
    
    
# for
for waiting_no in range(1,6):  
    print(f"대기번호 : {waiting_no}")   

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print(" {} 커피가 준비되었습니다".format(customer))
    
# 한 줄 for문
str = ["a", "b", "c", "d"]
str = [i.upper() for i in str]
print(str)

num = [1,2,3,4,5]
num = [i+100 for i in num]
print(num)


# while
customer = "토르"
index = 5
while index >= 1:
    print(f"{customer} 커피가 준비되었습니다 {index}번 남았습니다")
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다")
        
# 무한루프    
# index = 0
# while True:           # crtr + c 로 종료
#     print(f"{index}")
#     index += 1
    

# continue 와 break
absent = [2, 5]
no_book =[7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 끝! {student} 교무실로 따라와")
        break
    print(f"{student} 책을 읽어봐")
    

# quiz
import random
cnt = 0
for i in range(1,51):
    time = random.randrange(5,51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[X] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        
print("총 탑승 승객 : {0}분".format(cnt))
    
