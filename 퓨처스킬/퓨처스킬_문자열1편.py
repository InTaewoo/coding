#1번 : 대문자로 바꿔주세요
word = input('단어입력 : ')
print(word.upper())

#2번 : 오타 수정하기
word = input('단어입력 : ')
print(word.replace('q','e'))

#3번 : 대문자만 지나가세요
def filter(a):
    lst=[]
    for i in range(0,len(a)):
        if a[i].isupper() == True:
            lst.append(a[i])
    return ''.join(lst)
print(filter('HelloWorld'))

#4번 : 대소문자 바꿔서 출력하기
def change(a):
    return a.swapcase()
print(change('abC'))

