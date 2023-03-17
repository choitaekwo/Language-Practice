print("python", "java", sep=", ", end="? ")    # separate
print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")   # 왼쪽정렬, 오른쪽정렬

# 은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))   # 빈 공간 0으로 채움


# 다양한 출력포맷

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이고, 자릿수 확보하기
# 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점을 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))



