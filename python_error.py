 
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
# 

# 4. python NameError
# 5. python ZeroDivisionError
# 6. python FileNotFoundError
# 7. python TypeError
# 8. python AttributeError
# 9. python KeyError 
# 10. python OverFlowError
# 11. 기타