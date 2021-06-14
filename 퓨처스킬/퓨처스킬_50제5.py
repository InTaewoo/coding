#1번 : sample
#리스트에서 랜덤하게 값을 가져오는 코드를 작성하세요.
from random import randint
ages=[12,12,13,14,15]
def sample(lst):
    return ages[randint(0,4)]
print(sample(ages))

#2번 : similarity
#두 리스트에 모두 있는 값들을 리스트로 반환하는 코드를 작성하세요.
lst1 = [1,2,3]
lst2 = [1,2,4]
def similarity(a,b):
    return list(set(lst1) & set(lst2))
print(similarity(lst1,lst2))

# a=[]
# def similarity1(a,b):
#    for i in a :
#        if i in b :
#            a.append(i)
#     return a
# print(similarity1(lst1,lst2))

#3번 : split lines
#줄 바꿈 이스케이프 코드(\n)로 나뉘어 여러 줄로 이루어진 문자열을
# 각각 리스트로 분할하는 코드를 작성하세요.
corpus = 'Sentence1\nSentence2\nSentence3'
def split_lines(corpus):
    return corpus.split('\n')
print(split_lines(corpus))

#4번 : sum by
#주어진 함수를 리스트의 각 값에 적용한 뒤, 합계를 반환하는 코드를 작성하세요.

lst = [{'n':4},{'n':2},{'n':8},{'n':6}]
fn = lambda v:v['n']

def sum_by(lst,fn):
    return sum(map(fn,lst))
print(sum_by(lst,fn))

#5번 : tail
lst = [1, 2, 3, 4, 5]

def tail(lst):
    return lst[1:]
print(tail(lst))

#6번 : take
#리스트의 앞에서부터의 n개 값을 가져와 반환하는 코드를 작성하세요.
def take(itr, n=1):
    return itr[:n]
print(take([1,2,3,4,5],3))
print(take([1,2,3],5))
print(take([1,2,3],0))

#7번 : take right
#리스트의 끝에서부터의 n개 값을 가져와 반환하는 코드를 작성하세요.
def take_right(itr,n=1):
    return itr[::-1][:n]
print(take_right([1,2,3,4,5],3))
print(take_right([1,2,3],5))
print(take_right([1,2,3]))

#8번 : union
#두 리스트에 하나라도 존재하는 값을 모두 반환하는 코드를 작성하세요.
a = [1,2,3,99]
b = [2,3,4,52]

def union(a,b):
    return sorted(list(set(a+b)))
print(union(a,b))

def union(a,b):
    return sorted(list(set(a).union(b)))
print(union(a,b))

#9번 : unique elements
#리스트에서 하나 이상의 중복된 값을 제거한 후 정렬하는 코드를 작성하세요.

lst = [1,4,4,4,5,5,2,3]

def unique_elements(lst):
    return list(set(lst))
print(unique_elements(lst))

#10번 : values only
#딕셔너리의 모든 값을 리스트로 변환하는 코드를 작성하세요.
ages = {
	"Peter":10,
	"Isabel":11,
	"Anna":9,
}

def values_only(flat_dict):
    return list(ages.values())
print(values_only(ages))