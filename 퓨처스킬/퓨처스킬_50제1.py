#2번 : all_unique
def all_unique(lst):
    if len(set(lst)) == len(lst):
        print(True)
    else :
        print(False)
all_unique([1, 2, 3, 4, 5, 6])
all_unique([1, 2, 2, 3, 4, 5])

#3번 : capitalize every word
s = "hello world"

def capitalize_every_word(s):
    return s.title()
print(capitalize_every_word(s))

#4번 : celsius to fahrenheit
celsius = 180
def celsius_to_fahrenheit(celsius):
    return (celsius*1.8)+32
print(celsius_to_fahrenheit(celsius))

#5번 : compact
lst = [0, 1, False, 2, '', 3, 'a', 's', 34]

def compact(lst):
    return list(filter(None,lst))
print(compact(lst))

#6번 : count occurences
lst = [1,1,2,1,2,3]

def count_occurences(lst, val):
    return lst.count(val)
print(count_occurences(lst,2))


def count_occurences(lst, val):
    count = 0
    for i in lst:
        if i == val :
            count+=1
    return count
print(count_occurences(lst,2))

#7번 : degrees to rads
from math import pi
degrees = 180

def degrees_to_rads(degrees):
    return (degrees*pi)/degrees
print(degrees_to_rads(degrees))

#8 difference
lst1 = [1,2,3]
lst2 = [1,2,4]
def difference(a,b):
    return list(set(a)-set(b))
print(difference(lst1,lst2))

#9번 : digitize
a=123
def digitize(n):
    return list(map(int,str(a)))
print(digitize(a))

#10번 drop
def drop(lst, n=1):
    return lst[n:]

print(drop([1,2,3]))
print(drop([1,2,3],2))
print(drop([1,2,3],42))
