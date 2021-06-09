#1번 : drop right
import collections


def drop_right(lst,n=1):
    return lst[:-n]

print(drop_right([1,2,3]))

#2번 : every nth
lst = [1,2,3,4,5,6]
a = []
def every_nth(lst,n):
    for i in lst :
        if i % n == 0 :
            a.append(i)
        else :
            pass
    return a
print(every_nth(lst,4))

#3번 : fahrenheit to celsius
fahrenheit = 77
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)/1.8
print(fahrenheit_to_celsius(77))

#4번 : filter non-unique
from collections import Counter
lst = [1,2,2,3,4,4,5]
a=[]
def filter_non_unique(lst):
    for i in lst:
        if lst.count(i)==1:
            a.append(i)
    return a
print(filter_non_unique(lst))

#5번 : filter unique
lst = [1,2,2,3,4,4,5]
a=[]
def filter_unique(lst):
    for i in lst :
        if lst.count(i)>1:
            a.append(i)
    return list(set(a))
print(filter_unique(lst))

#6번 : for each
itr = [1,2,3]
fn = print

def for_each(itr,fn):
    for i in itr:
        fn(i)

print(for_each(itr, print))

#7번 : for each right
itr = [1,2,3]

def for_each_right(itr, fn):
    for i in itr[::-1]:
        fn(i)
print(for_each_right(itr,print))

# 8번 : has duplicates
lst = [1,2,3]

def has_duplicates(lst):
    for i in lst :
        if lst.count(i) > 1 :
            return True
        else :
            return False
print(has_duplicates(lst))

#9번 : head
lst = [1,2,3]
def head(lst):
    return lst[0]
print(head(lst))

#10번 : in range
def in_range(n, start, end=0):
    if start < n < end :
        return True
    else :
        return False
print(in_range(3,2,5))
print(in_range(3,4))