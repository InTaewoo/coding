# #1번 : 평균 점수
#
# def avg():
#     score=list(map(int,input('점수를 입력하시오').split()))
#     avgs = sum(score)/len(score)
#     print(f'{avgs:.0f}')
# avg()
#
# #2번 : 제곱을 구하자
# def mul():
#     num = list(map(int,input('숫자 입력 : ').split()))
#     muls = num[0] ** num[1]
#     print(muls)
# mul()
#
# for i in range(2):
#     n,m = map(int,input().split())
#     print(n**m)

# #3번 : 몫과 나머지
# for num in range(2):
#     a,b=map(int,input('숫자를 입력하시오 : ').split())
#     print(a//b,a%b)

#4번 : 원의 넓이를 구하세요
# import math
# def cir_area():
#     a = int(input('반지름을 입력하시오 : '))
#     print(a*a*math.pi)
# cir_area()

#5번 : Time 함수 사용하기
# from datetime import datetime
# print(datetime.today().year)
# print(datetime.today().strftime('%Y'))
#
# #6번 : 최대값 구하기
# for num in range(2):
#    print(max(map(int,input('숫자를 입력하시오 : ').split())))
#
#7번 : 반 평균 등수
import random  as r

score = []
class_score = []

for i in range(5):
   score.append(r.randint(1, 100))
print(score)

for i in range(0,30):
   class_score.append(r.randint(1,100))
print(class_score)
