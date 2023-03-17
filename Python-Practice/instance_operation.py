# isinstance() 함수
class Test1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"my name is {self.name}. I am {self.age} years old"
    
    # def __repr__(self):
    #     return f"my name is {self.name}. I am {self.age} years old"

t1 = Test1("CHOI", 22)

print(isinstance(t1, Test1))
print(isinstance(3, int))
print(isinstance([1, 2, 3], list))

# __str__() 함수
print(t1)  # 객체를 넘겨주면 __str__()이 호출됨. 클래스 내에 정의 안해주면 주소만 출력

# __repr__() 함수
print(t1)  # 클래스 내에 __str__() 정의되어있지 않으면 __repr__()이 호출됨 (__str__이 우선임)


# 객체 사이의 산술 연산
class LengthClass:
    def __init__(self, meter, centimeter):
        self.meter = meter
        self.centimeter = centimeter
    
    #__add__() 함수
    def __add__(self, other):  # self 다음에 다른 객체 other
        f = self.meter + other.meter
        i = self.centimeter + other.centimeter
        return f + i/100
    
    # __sub__() 함수
    def __sub__(self, other):
        f = other.meter - self.meter 
        i = other.meter - self.centimeter
        return f + i/100
    
    # __mul__() 함수
    def __mul__(self, other):
        f = self.meter * other.meter
        i = self.centimeter * other.centimeter
        return f + i/100
        
    # __truediv__() 함수
    def __truediv__(self, other):
        f = other.meter / self.meter 
        i = other.meter / self.centimeter
        return f + i/100
    
    # __floordiv__() 함수
    def __floordiv__(self, other):
        f = other.meter // self.meter 
        i = other.meter // self.centimeter
        return f + i/100
    
    # __mod__() 함수
    def __mod__(self, other):
        f = other.meter % self.meter 
        i = other.meter % self.centimeter
        return f + i/100
    
    # 객체 사이의 비교 연산
    # __eq__() 함수
    def __eq__(self, other):
        if self.meter == other.meter and self.centimeter == other.centimeter:
            return True
        else:
            return False 
    
    # __lt__() 함수
    def __lt__(self, other):
        x = self.meter * 100 + self.centimeter
        y = other.meter * 100 + other.centimeter
        if x > y:
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.meter) + "m " + str(self.centimeter) + "cm"
    
length1 = LengthClass(1, 30)
length2 = LengthClass(2, 93)
print(f"length1의 길이는 {length1}입니다")  # __str__() 함수 호출
print(f"length1 + length2 = {length1 + length2}미터입니다")  # 객체 사이의 합 __add__()
print(f"length1 - length2 = {length1 - length2}미터입니다")  # 객체 사이의 뺄셈 __sub__()
print(f"length1 * length2 = {length1 * length2}미터입니다")  # 객체 사이의 곱셈 __mul__()
print(f"length1 / length2 = {length1 / length2}미터입니다")  # 객체 사이의 나눗셈 __truediv__()
print(f"length1 // length2 = {length1 // length2}미터입니다")  # 객체 사이의 몫 연산 __floordiv__()
print(f"length1 % length2 = {length1 % length2}미터입니다")  # 객체 사이의 나머지 연산 __mod__()

# 객체 사이의 비교 연산
print(f"length1 == length2 ? {length1 == length2}")
print(f"length1 > length2 ? {length1 > length2}")