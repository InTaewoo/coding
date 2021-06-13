#1번 : max element index
#리스트에서 가장 큰 값의 인덱스를 반환하는 코드를 작성하세요.
lst = [5,8,9,7,10,3,0]
def max_element_index(lst):
    return lst.index(max(lst))
print(max_element_index(lst))

#2번 : max n
#리스트에서 큰 순서대로 n개의 값을 반환하는 코드를 작성하세요.

def max_n(lst,n=1):
    return sorted(lst,reverse=True)[:n]
print(max_n([1,2,3]))
print(max_n([1,2,3], 2))


def max_n(lst, n=1):
    a=[]
    for i in range(n):
        add = lst.pop(lst.index(max(lst)))
        a.append(add)
    return a
print(max_n([1,2,3]))

#3번 : median
#숫자로 구성된 리스트에서 중앙값(median)을 반환하는 코드를 작성하세요.

def median(lst):
    return sum(lst)/len(lst)
print(median([1,2,3]))
print(median([1,2,3,4]))

#4번 : min by
#주어진 함수를 리스트의 각 값에 적용한 뒤, 최솟값을 반환하는 코드를 작성하세요.

lst = [{'n':4},{'n':2},{'n':8},{'n':6}]
fn = lambda v:v['n']

def min_by(lst, fn):
    return min(map(fn,lst))
print(min_by(lst,fn))

#5번 : min n
#리스트에서 작은 순서대로 n개의 값을 반환하는 코드를 작성하세요.

def min_n(lst,n=1):
    return sorted(lst)[:n]
print(min_n([1,2,3]))
print(min_n([1,2,3], 2))

#6번 : most frequent
#리스트에서 가장 많이 등장하는 값을 반환하는 코드를 작성하세요.

def most_frequent(lst):
    return max(set(lst),key=lst.count)
print(most_frequent([1,2,3,4,4]))
print(most_frequent([1,2,1,2,3,2,1,4,2]))

#7번 : n time string
#주어진 개수만큼 동일한 문자열을 출력하는 코드를 작성하세요.
def n_time_string(s,n):
    return str(s)*4
print(n_time_string('py',4))

#8번 : offset
#주어진 수(n)만큼의 값을 리스트의 끝으로 이동시키는 코드를 작성하세요.

def offset(lst,n):
    return lst[n:] + lst[:n]
print(offset([1,2,3],1))
print(offset([3,4,5,6,7],2))

#9번 : rads to degrees
from math import pi
def rads_to_degrees(rad):
    return (rad * 180.0) / math.pi

print(rads_to_degrees(math.pi/2))

#10번 : reverse string
s="snippet"

def reverse_string(s):
    return s[::-1]

print(reverse_string(s))