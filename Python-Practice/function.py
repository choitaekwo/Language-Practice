def open_account():
    print("새로운 계좌가 생성되었습니다")
    
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance
    
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money -commission   # 여러 개 반환 가능 (tuple 로 반환)

balance = 0  # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 200)
commission, balance = withdraw_night(balance, 500)
print(f"수수료 {commission}이며, 잔액은 {balance}입니다")

# 기본값 설정
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t메인 언어 : {2}"\
        .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")

# 키워드값
def profile2(name, age, main_lang):
    print(name, age, main_lang)
    
profile2(name="유재석", main_lang="파이썬", age=20)
profile2(main_lang="자바", age=25, name="김태호")
    
# 가변인자
# def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}\t나이 : {age}\t언어 : {lang1}, {lang2}, {lang3}, {lang4}, {lang5}")
    
def profile3(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t언어 : ", end=" ")   # end=" " 줄 안바꾸고 출력 가능
    for lang in language:
        print(lang, end=" ")
    print()
    
profile3("유재석", 20, "python", "java", "C", "C++", "Ruby")
profile3("김태호", 25, "python", "java")             # 5개보다 적거나
profile3("유재석", 20, "python", "java", "C", "C++", "Ruby", "javascript")  # 5개보다 많거나


# quiz
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
        
    elif gender == "여자":
        return height * height * 21

gender = input("성별을 입력하세요 : ")
height = input("키를 입력하세요 : ")
height = int(height)
       
# height = 167
# gender = "남자"
weight = round(std_weight(height / 100, gender), 2)   

print("키 {0}cm {1}의 표준 체중은 {2}kg입나다".format(height, gender, weight))

