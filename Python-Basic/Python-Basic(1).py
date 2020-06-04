print("멋쟁이 사자처럼")
print(1+2)

#----------
class_monitor = "성준"
print("우리 반장 이름은?", class_monitor)

#----------
rain = "꾸러기 표정을 지었나요?"
print("1일 1깡 : ", rain)

rain = "화려한 조명이 감쌌나요?"
print("1일 1깡 : ", rain)

#----------
gang = input()
print("1일 1깡 : ", gang)

#---------- str type input
number1 = input("첫번째 숫자를 입력하세요 : ")
number2 = input("두번째 숫자를 입력하세요 : ")

print(number1 + number2)

#---------- int type input
number1 = int(input("첫번째 숫자를 입력하세요 : "))
number2 = int(input("두번째 숫자를 입력하세요 : "))

print(number1 + number2)

#---------- import 사용하기
import random

print(random.random())
# random range 지정
print(random.randrange(1,7))
print(random.randrange(1,7))
print(random.randrange(1,7))

#---------- 사칙연산
a = 2
b = 5

print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a**b=",a**b)
print("b%a=",b%a)
print("b/a=",b/a)
print("b//s=",b//a)

#---------- 이름, 학번, 학과 한 줄로 출력하기
name = input("name: ")
number = input("student number: ")
major = input("department: ")
print (name, number, major)
print (name, end=' ')
print (number, end=' ')
print (major, end=' ')