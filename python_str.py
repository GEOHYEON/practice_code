# string의 객체 함수를 정리한 파일입니다.

# dir: str 문자열 객체의 메서드 출력
dir(str)

# help(): str 문자열 객체 메소드 사용법
help(str.upper)

test1 = 'Hello Python'
test2 = 'hello python'
# upper(): 모두 대문자로 바꿈
# lower(): 모두 소문자로 바꿈
# swapcase(): 대문자는 소문자로, 소문자는 대문자로 바꿈
# capitalize(): 첫 글자를 대문자로 바꿈
# title(): 각 단어를 대문자로 바꿈
test1.upper()
test1.lower()
test1.swapcase()
test2.capitalize()
test2.title()


test3 = '!@##   Oh my@@god!   !@#!@#'
# strip(str): 양쪽 끝 부터 str에 포함된 문자열이 발견되지 않을때까지 자름.
# lstrip(str):왼쪽 끝 부터 str에 포함된 문자열이 발견되지 않을때까지 자름.
# rstrip(str): 오른쪽 끝 부터 str에 포함된 문자열이 발견되지 않을때까지 자름.
test3.strip("!@#$ ")
test3.lstrip("!@#$ ")
test3.rstrip("!@#$ ")