# #1번 : 놀이기구 키 제한
# tall = int(input('키를 입력하시오 : '))
# if tall > 150 :
#     print(True)
# else :
#     print(False)
#
# #2번 : 3의 배수 인가요
# a = int(input('숫자 : '))
# if a % 3 == 0 :
#     print('짝')
# else :
#     print(a)
#
# #3번 : 배수인지 확인하기
# i = 7
# if i % 6 == 0 :
#     print(True)
# else :
#     print(False)

#4번 : 연속되는 수
#숫자가 공백으로 구분되어 주어지면, 이 숫자의 배열이 연속수인지 아닌지
# True/False 로 판별하는 코드를 작성해주세요.
# (단, 자연수와 음수를 포함한 정수를 입력으로 받으며, 연속인지 아닌지의 기준은 정수를 기준으로 한다.)

def check(a): # func checks if numbers are continuous
    cnt = 1
    for i in range(len(a) - 1):
        if a[i] + 1 == a[i+1]: # set gap as +1
            cnt += 1
        else:
            break
    # print(cnt, len(a))
    if cnt == len(a): # compare cnt & len(a)
        return True
    else:
        return False

num = input().split()

for i in range(len(num)):
    try: # if available to transform
        num[i] = int(num[i])
    except:
        print("정수가 아닌 수가 있습니다.")
        quit()

num.sort() # sort ascending
print(check(num))




