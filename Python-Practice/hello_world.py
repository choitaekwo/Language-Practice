print("hello world")
a = "hello"
b = "world"
print(f"{a} {b}")
print(a + " " + b)
print("{} {}".format(a,b))
print("%s %s" % ("hello", "world"))

import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/USER/Desktop/project/log_sort2/fft.asis.pac.csv")
print(data)
print(data.head(3))
print(data.describe())


# list 인덱스(음수) 활용
list = [1,2,3,4,5,6,7,8,9,10]
print(list)              
print(list[::2])          # [1, 3, 5, 7, 9]
print(list[-1])           # 10  (뒤에서 첫 번째)
print(list[-5])           # 6   (뒤에서 다섯 번째)
print(list[-5:])          # [6, 7, 8, 9, 10]
print(list[-5::2])        # [6, 8, 10]
print(list[-5:-8:-1])     # [6, 5, 4]
print(list[::-1])         # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

