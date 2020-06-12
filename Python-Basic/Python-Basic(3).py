# 리스트
li = [3, 1, '배가', 4, '고파요', 5, 1]
# 인덱싱
print(li[2])
# 슬라이싱
print(li[0:3])

# 리스트 (내장함수)
li = [3, 1, '배가', 4, '고파요', 5, 1]
li_2 = [3, 1, 2, 4, 9, 5, 1]
# 리스트의 길이를 구해주는 함수 - len(변수)
print(len(li))
# 리스트 원소를 오름차순으로 정렬해주는 함수 - 변수.sort()
li_2.sort()
print(li_2)
# 리스트 내의 특정 원소 인덱스를 반환해주는 함수 - 변수.index()
print(li.index("고파요"))
# 리스트 내의 특정 원소의 개수 세기 - 변수.count(특정 원소)
print(li.count(1))

# 딕셔너리(내장함수)
pairs = {'지코': '아무노래', '오반': '어떻게 지내', '크러쉬': '가끔'}
print(pairs)
# 하나의 key-value 쌍을 추가하는 방법
# 딕셔너리형 변수 [key] = value
pairs['Maroon 5'] = 'Memories'
# 4번째 key-value 쌍을 추가했어요!
print(pairs)
# 특정 key-value 삭제하는 방법 : del 함수
del pairs['지코']
print(pairs)
# key로 value 얻기 : 변수.get(key)
v = pairs.get('오반')
print(v)

#튜플 생성
tp = (1, 2, 3)
tp2 = (4, 5, 6)
#튜플의 덧셈
print(tp + tp2)
#튜플의 곱셈
print(tp * 3)
#튜플의 인덱싱
print(tp[0])
#튜플의 슬라이싱
print(tp[0:3])

# 조건문
solution = input("12 + 3 = ")
if(solution == "15"):
    print("정답입니다!")
else:
    print("틀렸어요.")
#---------------------------------------------------
score = int(input("점수를 입력해 주세요 : "))
if(score >= 85):
    print("PASS")
else:
    print("FAIL")
#---------------------------------------------------
tangsuyuk = input("너 부먹이야?\n")
if(tangsuyuk == "부먹"):
    print("----상대방이 대화방을 나갔습니다.----")
elif(tangsuyuk == "찍먹"):
    print("♥"*3)
else:
    print("나는 찍먹이야")
#---------------------------------------------------
money = (int(input("돈 얼마 있어? ")))
if(money >= 5000):
    print("아웃백 가자")
elif(money >= 3000):
    print("학식 먹자")
elif(money >= 1000):
    print("컵라면 먹자")
else:
    print("공깃밥 가즈아")

# 반복문 (for문)
for score in [96, 98, 100, 87]:
	print(score)
# for문에서 유용한 range 함수
sum = 0
for i in range(5):
	sum += i
# 반복문 (while문)
num = 10
while(num > 0):
	print("반복문 수행 중!")
	num -= 1
# while문에 true를 넣으면 무한 루프가 생성되고, break를 종료시킬 수 있음
num = 0

while(True):  # true 대신에 1을 써도 됨
    num += 1
    if(num > 10):
        print(num, "멈춰")
        break

# 함수
def plusOne(x):
    return x + 1

mayBeSix = plusOne(5)
print(mayBeSix)
#---------------------------------------------------
def plus(x, y):
    return x+y

x = plus(10, 20)
print(x)


# 전역변수, 지역변수 이해하기
x = 10          # 전역 변수
def foo():
    x = 20      # x는 foo의 지역 변수
    print(x)    # foo의 지역 변수 출력

foo()
print(x)        # 전역 변수 출력
# 20
# 10
#---------------------------------------------------
x = 10          # 전역 변수
def foo2():
    global x    # 전역 변수 x를 사용하겠다고 설정
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력

foo2()
print(x)        # 전역 변수 출력
# 20
# 20

#---------------------------------------------------
a = 2
def test() :
    global b 
    b = 34
    c = 50
    print("inside test", a)
    print("inside test", b)
    print("inside test", c)

test()
print("after test", a)
print("after test", b)
# print("after test", c)
# c는 test 함수 안에 있는 지역변수이기 때문에 error