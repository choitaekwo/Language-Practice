sentence = "나는 소년입니다"
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요"""
print(sentence3)         # 여러 줄 출력

print("hello world " * 100)     #문자열 반복
print(len("hello world " * 100))  #문자열 길이
print("hello world".replace("world", "universe"))  #문자 치환


# 슬라이싱
jumin_number = "010130-1234567"
print("성별 : " + jumin_number[7]) 
print("연 : " + jumin_number[0:2]) # 0번째부터 n-1 번째까지
print("월 : " + jumin_number[2:4])
print("일 : " + jumin_number[4:6])
print("생년월일 : " + jumin_number[:6])  # 처음부터
print("뒤 7자리 : " + jumin_number[7:])  # 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin_number[-7:]) # 맨 뒤에서 7번째부터 끝까지 


# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())   # 소문자로 출력
print(python.upper())   # 대문자로 출력
print(python[0].isupper())  # True

print(len(python))    # 17

print(python.replace("Amazing", "Powerful"))  # 치환

index = python.index("n")  # 5
print(index)
index2 = python.index("n", index + 1)  # index + 1 (6)부터 n을 찾기
print(index2)

print(python.find("n"))   # 5
print(python.find("Java"))  # -1 반환 
#print(python.index("Java")) # 오류 발생

print(python.count("n"))  # "n" 이 몇 번 있는지


# 문자열 포멧

# 방법 1
# print("나는 %d살입니다" % 20)
# print("나는 %s를 좋아해요" % "파이썬")
# print("Apple은 %c로 시작해요" % "A")   
print("나는 %s살입니다" % 20)          # %s 로 다 써도됨
print("나는 %s색과 %s색을 좋아해요" % ("파랑", "빨강"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파랑", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("파랑", "빨강"))
print("나는 {2}색과 {1}색과 {0}색을 좋아해요".format("파랑", "빨강", "노랑"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨강"))

# 방법 4
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요")


#  탈출 문자

print("백문이 불여일견\n백견이 불여일타")  # \n : 줄바꿈

# 저는 "나도코딩"입니다.
print("저는 \"나도코딩\"입니다.")   # \", \' : 문장 내에서 따옴표
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\User\\Desktop\\python practice")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


# (quiz) 비밀번호 만들기
url = "http://" + input("사이트 이름 : ") + ".com"
site = url[7:]
site2 = site[:-4]
password = site2[:3] +  str(len(site2)) + str(site2.count("e")) + "!"
print(f"{url}의 비밀번호는 {password}입니다")
print("{0}의 비밀번호는 {1}입니다".format(url, password))

