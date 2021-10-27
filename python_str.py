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

test4 = "i\'m good"
# replace(str_A, str_B): A string 을 B string 으로 변경
# format(str, ...): format에 string 집어넣음
# str_target.join(str, ...): 매개변수 사이에 str_target을 집어넣음

test4.replace('good', 'bad')
'{}\'m {}'.format('i', 'good')
'@@'.join(['HI', 'YES'])

test5 = 'Hello, World'
# center(int, default= " "): int size 문자열에서 중앙정렬
# rjust(int, default= " "): int size 문자열에서 오른쪽 정렬
# ljust(int, default=" "): int size 문자열에서 왼쪽 정렬
# zfill(int): int size에서 남는 사이즈 만큼 0 붙임

test5.center(30, "!")
test5.rjust(30, "!")
test5.ljust(30, "!")
test5.zfill(30)


test6 = 'car apple banana'
# partition은 한번만 나눔
# partition(str): 전달된 문자로 문자열을 나눔, return tuple
# rpartition(str): 뒤에서부터 전달한 인자로 문자열을 나눔
# split(str, n): 전달한 문자로 문자열을 n번 나눔. return list
# rsplit(str, n): 뒤에서 부터 전달한 문자로 문자열을 n번 나눔. return list
# splitline(): line별로 나눔

test6.partition(" ")
test6.rpartition(" ")
test6.split(" ")
test6.split(" ", 1)
test6.rsplit(" ", 1)

test7 = "Hello,\nmy name is NOH\nThis is my exercise.\nHow are you?"
test7.splitlines()

# 문자열 판단
# isalnum() - 알파벳 또는 숫자인가? 
# isalpha() - 알파벳인가?
# isdecimal() - 숫자(decimal, 10진수)인가?
# isdigit() - 숫자(digit, 10진수)인가?
# isidentifier() - 식별자로 사용 가능한가?
# islower() - 소문자인가? 
# isnumeric() - 숫자인가? 
# isspace() - 공백인가? 
# istitle() - title 형식인가? (단어마다 첫 글자가 대문자인가?)
# isupper() - 대문자인가?

test8 = "abc123"
test9 = "abc"
test10 = "123 "
test11 = " "

test8.isalnum()
test9.isalpha()
test10.isdecimal()
test10.isspace()
test11.isspace()

# count() - 특정 단어(문자열)의 수를 구함 (없으면 0을 반환)
# startswith() - 특정 단어로 시작하는지 확인
# endswith() - 특정 단어로 끝나는지 확인

test12 = "hi hello hi hi hi"

test12.count("hi")
test12.startswith("hi")
test12.startswith("hello")
test12.endswith("hi")

