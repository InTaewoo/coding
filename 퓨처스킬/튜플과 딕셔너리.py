#1번 : 튜플 기본 구조 (자료형)
my_tuple1 = ()
print(my_tuple1)

my_tuple2 = (1, -2, 3.14)
print(my_tuple2)

my_tuple3 = '앨리스', 10, 1.0, 1.2
print(my_tuple3)
('앨리스', 10, 1.0, 1.2)

my_tuple = (1,)
print(type(my_tuple))

#2번 : 값 가져오기 (자료형)
#
# clovers = ('클로버1','하트2','클로버3')
# print(clovers(1))

#3번 : 패킹과 언패킹 (자료형)

clovers = '클로버1','하트2','클로버3'
print(clovers)
('클로버1','하트2','클로버3')

# 언패킹

alice_blue = (240,248,255)
r,g,b = alice_blue
print('R', r, 'G', g, 'B', b)

#4번 : 박하맛 사탕 바꿔주기 (자료형)
dodo ='박하맛'
alice ='딸기맛'

print('도도새 :',dodo,'앨리스:',alice)
dodo,alice=alice,dodo
print('도도새 :',dodo,'앨리스:',alice)

#5번 : 딕셔너리 기본 구조 (자료형)
my_dict1 = {}
print(my_dict1)

my_dict2 = {0:1, 1:-2, 2:3.14}
print(my_dict2)

my_dict3 = {'이름':'앨리스','나이':10,'시력':[1.0, 1.2]}
print(my_dict3)

my_dict = {}
print(type(my_dict))

#6번 : 키 값 추가하기 (자료형)
clover = {'나이':27,'직업':'병사'}
clover['번호']=9
print(clover)
print(clover.get('번호'))

#7번 : 값에 접근하기 (자료형)

clover = {'나이':27,'직업':'병사','번호':9}
print(clover['번호'])
clover['번호'] = 6
print(clover['번호'])
print(clover.get('번호'))

#8번 : 키 값 제거하기 (자료형)

clover = {'나이':27,'직업':'병사','번호':9}
del clover['나이']
print(clover)

#9번 : 3월 토끼의 라면가게 (자료형)

orders = {'스페이드1':'비빔라면','다이아2':'매운라면'}
print(orders)
orders['클로버3']='카레라면'
print(orders)
orders['다이아2']='짜장라면'
print(orders)
del orders['스페이드1']
print(orders)
