# 파일 입출력
score_file = open("score.txt", "w", encoding = "utf-8")  # wrtie
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()      # 열었으면 항상 닫아줘야함

score_file = open("score.txt", "a", encoding="utf-8")   # append
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")   # read
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()   # list 형태로 저장
for line in lines:
    print(line, end="")

print("\n")
score_file.close()


# pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile_load = pickle.load(profile_file)  # file에 있는 정보를 profile_load에 불러옴
# print(profile_load)
# profile_load.close()


# with
with open("study.txt", "w", encoding="utf-8") as study_file:  # 파일 쓰기
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:  # 파일 읽기
    print(study_file.read())
    
# close 안해도됨 알아서 종료해줌

# quiz
for i in range(1,11):
    with open(str(i) + "주차.txt", "w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -\n".format(i))
        report_file.write("부서 :\n")
        report_file.write("이름 :\n")
        report_file.write("업무 요약 :")
        
        


