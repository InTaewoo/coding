#1번 : 리스트의 삭제
nums = [100, 200, 300, 400, 500]
del nums[3:5]
print(nums)

#2번 : 리스트의 내장함수
nums = [200,100,300]
nums.insert(2,10000)
print(nums)

#3번 : 변형된 리스트
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
print(list(map(lambda x,y:[x,y],a,b)))
c=list(zip(a,b))

#4번 : enumerate
student = ['강은지','김유정','박현서','최성훈','홍유진',
           '박지호','권윤일','김채리','한지호','김진이',
           '김민호','강채연']
for i,v in enumerate(student,1):
    print(f'번호: {i}, 이름: {v}')
