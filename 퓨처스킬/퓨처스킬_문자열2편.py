#1번 : 2-gram
def gram(a) :
    for i in range(len(a)-1):
        print(a[i]+a[i+1])
print(gram('python'))

#2번 : 문자열 만들기
def split(a):
    print(len(a.split(' ')))
split('안녕하세요. 저는 퓨쳐스킬대학교 인공지능전공 김유진입니다.')

# #3번 : Count 사용하기
from collections import Counter
name = input("이름을 입력하시오 : ").split(' ')
counter = Counter(name).most_common()
print(counter[0][0]+'(이)가 총 {0}표 중 {1}표로 반장이 되었습니다.'.format(len(name),counter[0][1]))

#4번 : 친해지고 싶어
a = input()
b = a.split()
for word in b:
    print(word[0].upper(), end="")
print()

#5번 : 문자열 압축하기
word = input('단어입력 : ')
ct= Counter(word).most_common()
print(ct[0][0]+ct[0][1])
