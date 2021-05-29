#1번 : 전국 거북이 마라톤 (반복문)
for i in range(0,5000):
    print('안녕 거북이',i)

#2번 : for 기본 구조 (반복문)
charcter= ['엘리스','도도새','3월토끼']
for charcters in charcter :
    print(charcters)

#3번 : 여왕의 크로켓 경기장 (반복문)
players = ['공작부인','흰 토끼','하트잭','모자장수']
for player in players :
    print('{0} 퇴장!'.format(player))

#4번 : 문자열 반복하기 (반복문)
cat = '체셔고양이'
for i in cat:
    print(i)

#5번 : 들여쓰기 (반복문)
# 코드1
nums = [0,1,2]
for num in nums :
	print(num)
print(nums)

# 코드2
nums = [0,1,2]
for num in nums :
	print(num)
	print(nums)

#6번 : 순서열 만들기 (반복문)
for i in range(1,10):
    print(2,'x',i,'=',2*i)

#7번 : 하얀장미와 빨간장미 (반복문)

roses = ['하얀장미','하얀장미','하얀장미']
for rose in range(0,3):
    roses[rose]='빨간장미'
print(roses)

