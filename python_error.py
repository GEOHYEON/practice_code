 
# 참고: https://blockdmask.tistory.com/550

# python의 대표 error 정리

# 1. python ValueError
# 부적절한 값을 가진 인자를 받았을 때 에러
try:
    num = int("BlockDMask") 
    print(f"number : {num}")
except ValueError:
    print("ValueError: num is not int")

try:
    arr = ['a', 'b', 'c', 'd', 'e'] 
    arr.index('z') # error
except ValueError:
    print("ValueError: \'z\' is not in arr")

# 2. python IndexError
# 인덱스 범위를 벗어나는 경우에 발생하는 에러

try:
    arr = ['a', 'b', 'c', 'd', 'e'] 
    arr[50]
except:
    print("index error")

# 3. python SyntaxError
# 파이썬 문법 오류가 발생하는 경우

# 4. python NameError
# 지역변수, 전역 변수 이름을 찾을 수 없는 경우

try:
    a = 1
    b = 2
    print(c)
except NameError:
    print("name \'c\' is not in here")



# 5. python ZeroDivisionError

try:
    a = 99 / 0
    print(a)
except ZeroDivisionError:
    print("ZeroDivisionError")


# 6. python FileNotFoundError
# 

try:
    f = open("FileNotFoundError.py", "r")
except FileNotFoundError as e:
    print("FileNotFoundError: ", e)


# 7. python TypeError
# 잘못된 타입을 전달했을 때 발생하는 에러

try: 
    a = 1 + "abc"   # type error
except TypeError as e:
    print("TypeError:", e)

# 8. python AttributeError
# 클래스(모듈)의 객체에 해당하는 메서드나 속성을 잘못 호출하거나 대입했을 때 발생하는 에러

import math

# 정상 접근
a = math.ceil(1.2)
print("Attribute 정상접근: ", a)

# math ceil2 라는 메서드는 없습니다.
try:    
    b = math.ceil2(1.2)
    print(b)
except AttributeError as e:
    print("AttributeError: ", e)

# 9. python KeyError 
# 딕셔너리에서 접근하려는 키 값이 없을 때 발생하는 에러

try:
    d = {"a": 12, "b": 33} # 없는 키값에 접근
    result = d["z"]
except KeyError as e:
    print("KeyError: ", e)

# 10. python OverFlowError
# 연산의 결과가 너무 커서 데이터 타입이 표현할 수 있는 숫자의 범위를 넘어가는 경우

try:
    a = 2 ** 123456
    b = 5 
    print(a / b)

except OverflowError as e:
    print("overflowerror", e)


# 11. 기타
# https://docs.python.org/ko/3/library/exceptions.html