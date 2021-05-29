#1번 : 참과 거짓 (자료형)
print(True)

print(False)
# 불리안 형태의 True와 False로 출력

#2번 : 값 비교하기 (자료형)
print(1 == 2)

#3번 : if 기본구조 (조건문)
score = 90
if score > 80 :
	print('합격입니다.')

#4번 : else 와 elif (조건문)
score = 75

if 80 < score <= 100:
	print('학점은 A입니다.')
elif 60 < score <= 80:
	print('학점은 B입니다.')
elif 40 < score <= 60:
	print('학점은 C입니다.')
else :
	print('학점은 F입니다.')

#5번 : 자동 입장료 계산기 (조건문)
total_price = 0
ages = [22,21,17,32,4,28,19,8]
for i in ages:
	if i >= 20:
		total_price+=8000
	elif 10 <= i <= 19 :
		total_price+=5000
	else :
		total_price+=2500
print('총 입장료는 {0}원 입니다.'.format(total_price))

#6번 : 여러 조건 판단하기 (조건문)
games = 12
points = 25
if games >= 10 and points >=20:
	print('MVP로 선정되었습니다.')

#7번 : 사탕 도둑을 잡아라 (조건문)
suspects = [['거위','새','암컷'],['푸들','개','수컷'],['비글','개','암컷']]
for suspect in suspects :
	if suspect[1]=='개' and suspect[2]=='암컷':
		print('범인은',suspect[0],'입니다')
