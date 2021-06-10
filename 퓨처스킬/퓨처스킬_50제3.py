#1번 : initial
#리스트의 마지막 원소 를 제외한 나머지 모든 원소를 반환하는 코드를 작성하세요.

lst = [1,2,3,4,5]

def initial(lst):
    return lst[:-1]
print(initial(lst))

#2번 : initialize list with range
#주어진 범위 만큼의 리스트를 생성하는 코드를 작성하세요.
#단, start 와 end 는 범위를 지정하며, step 은 원소간의 간격을 의미합니다.


def initialize_list_with_range(end, start=0, step=1):
    return list(range(start,end+1,step))

print(initialize_list_with_range(5))
print(initialize_list_with_range(7,3))
print(initialize_list_with_range(9,0,2))

#3번 : initialize list with values
#주어진 값으로 채워진 리스트를 생성하는 코드를 작성하세요.
def initialize_list_with_values(n, val=0):
    return [val for i in range(n)]

print(initialize_list_with_values(5))
print(initialize_list_with_values(5,2))
print(initialize_list_with_range(3,3))


#4번 : intersection
#두 리스트에 모두 존재하는 값을 반환하는 코드를 작성하세요.
lst1 = [1,2,3]
lst2 = [2,3,4]

def intersection(a,b):
    return list((set(lst1) & set(lst2)))
print(intersection(lst1,lst2))

#5번 : is divisible
#첫번째 숫자(dividend)가 두번째 숫자(divisor)로 나누어 떨어지는지 확인하는 코드를 작성하세요.
a = int(input('a는 : '))
b = int(input('b는 : '))
def is_divisible(dividend, divisor):
    if a % b == 0 :
        return True
    else :
        return False
print(is_divisible(a,b))

#6번 : is even
#주어진 숫자가 짝수일 경우 True를, 홀수인 경우 False를 반환하는 코드를 작성하세요.

a = 9

def is_even(num):
    if a % 2 ==0:
        return True
    else :
        return False
print(is_even(a))

#7번 : is odd
#주어진 숫자가 홀수일 경우 True를, 짝수인 경우 False를 반환하는 코드를 작성하세요.
a = 4
def is_odd(num):
    return a % 2 != 0
print(is_odd(a))

#8번 : keys only
#딕셔너리의 모든 키를 리스트로 변환하는 코드를 작성하세요.
ages = {
	"Peter":10,
	"Isabel":11,
	"Anna":9,
}

def keys_only(flat_dict):
    return list(ages.keys())
print(keys_only(ages))

#9번 : last
#리스트의 마지막 값을 반환하는 코드를 작성하세요.

lst = [1,2,3]
def last(lst):
	return lst[-1]
print(last(lst))

#10번 : max by
#주어진 함수 fn를 리스트 lst의 각 값에 적용한 뒤, 최댓값을 반환하는 코드를 작성하세요.
lst = [{'n':4},{'n':2},{'n':8},{'n':6}]
fn = lambda v:v['n']

def max_by(lst, fn):
	return max(map(fn,lst))

print(max_by(lst,fn))