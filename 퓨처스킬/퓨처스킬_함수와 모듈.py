#1번 : 함수의 기본 구조 (함수)

def add (num1, num2) :
	return num1 + num2

print(add(2,3))

#2번 : 좀 더 효율적인 판결 (함수)

def judge_cards(name):
    for i in range(1,4):
        print(f'{name}{i} 유죄!')
judge_cards('하트')
judge_cards('클로버')
judge_cards('스페이드')

#3번 : 랜덤하게 뽑기 (모듈)

import random
animals = ['체셔고양이','오리','도도새']
animal=random.choice(animals)
aniMal = [random.choice(animals) for i in range(0,2)] #랜덤으로 2개 중복허용
print(aniMal)
print(animal)

#4번 : 하트 여왕의 판결 (모듈)

import random
cards = ['하트','클로버','스페이드']

card = random.choice(cards)
print(card,'유죄!')