# #1번 : while 기본구조 (반복문)
# for num in range(3) :
# 	print('안녕 거북이', num)
#
# while True:
#     for num in range(3):
#         print('안녕 거북이',num)
#     break
#
# #2번 : 이건 공평하지 않아 (반복문)
# count=0
# while True :
#     for count in range(1,6):
#         print('{0} 번째 바퀴입니다.'.format(count))
#     break
# print('경주 끝!')
#
# #3번 : 입력을 받는 방법 (입출력)
# name = input('이름이 뭐에요?')
# print(name,'안녕')
#
# #4번 : 앨리스의 수수께끼 (입출력)
#
# while True :
#     answer = input('영국의 수도는 어디일까요? ')
#     if answer == '런던':
#         break
# print('정답입니다')

#5번 : 넘어가기와 멈추기 (반복문)
# count = 0
# while count < 3:
# 	count = count + 1
# 	if count == 2:
# 		break
# 	print(count)
#
# #6번 : 무한 반복하기 (반복문)
# while True :
# 	print('Ctrl+C를 누르세요.')

#7
while True :
	answer = input('런던, 파리, 서울 중 영국의 수도는 어디일까요?')
	if answer == '서울':
		print('{0}은 대한민국의 수도입니다.'.format(answer))
	elif answer == '런던':
		print('정답입니다. 런던은 영국의 수도입니다.')
		break
	else :
		print('보기에서 골라주세요.')


