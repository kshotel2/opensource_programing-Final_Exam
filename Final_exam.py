#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201891 이름 : 강지민

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    if target in my_string: #03-1 if문 p.9 문자열 in 문자열
            #target 문자열이 my_string에 포함되어 있으면
        answer = 1
    else:   #아니면
        answer = 0
    return answer



# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''
    li_letter = letter.split()    #02-2 p.28 split 리스트화 
    i = 0
    while i < len(li_letter):  #02-3 p.9 len 함수 리스트
        answer = answer + morse[li_letter[i]]
        #02-2 p.11 문자열 더하기 02-5 p.6 딕셔너리 key로 value 얻기 
        #해독 된 문자열을 전(前) 문자열에 더하여서 초기화
        i=i+1   #리스트의 다음 요소 읽기
    return answer

letter = '-. --- .--. .- .. -. -. --- --. .- .. -.'
solution(letter)

# Q.3 10점
#
# PROGRAMMERS-857 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    answer = ''
    #각 숫자에 해당하는 알파벳을 딕셔너리로 선언(key도 문자)
    d_age = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', 
            '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
    li_age = []
    i=0
    #03-3 p.22 for문, 02-2 p.18 format 
    for i in "{}".format(age):  #포멧함수 이용 age문자열 변환
        li_age.append(i)        #for문의 문자열 하나씩 읽는 특성 이용하여 li_age에 append
    j=0
    while j < len(li_age):  #02-3 p.9 len 함수
        #02-2 p.11 문자열 더하기, 02-5 p.6 딕셔너리
        answer = answer + d_age[li_age[j]]  #key로 value 얻기 
        j=j+1
    return answer

def solution(age):
    answer = ''
    #각 숫자에 해당하는 알파벳을 딕셔너리로 선언(key 정수형)
    d_age = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    if age == 1000:     #1000이 최대값 특정하여 리턴
        answer = 'baaa'
    else:
        #03-1 p.8 if 문 and
        if age >= 100 and age < 1000:    #세 자리수 일 때
            # 02-1 p.6 몫을 리턴 '//', 02-2 p.11 문자열 더하기
            answer += d_age[age//100]       #딕셔너리에서 key인 100의 자리수에 대한 value 값
            answer += d_age[(age%100)//10] #10의 자리수에 댄한 value 값
            answer += d_age[(age%100)%10]  #1의 자리수에 대한 value 값
        else:
            if age >= 10 and age < 100:       #두 자리수 일 때
                answer += d_age[age//10]    #10의 자리수에 댄한 value 값
                answer += d_age[age%10]     #1의 자리수에 대한 value 값
            else:
                answer += d_age[age]    #한 자리수 일 때 key age에 대한 value 값
    return answer

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

#1. 원 안에 있는 정수 점의 갯수 구하기
#2. 첫 원에서 두번째 원 갯수 빼기
#좌표 xy값의 sqrt(x^2+y^2)이 r을 안넘으면 됨  
#y값을 변경하여 x값을 정할 때 x = sqrt(r^2-y^2)
#r1 작은 원 r2 큰 원
def solution(r1, r2):
    answer = 0
    for x in range(1, r2):   #r2 안의 모든 정수 좌표 구하는 for 문
        answer+=4*(((r2**2-x**2)**0.5)//1)  
        #r2 한 x좌표에 존재하는 정수 좌표의 개수는 
        #그 x좌표에 대한 원의 y좌표 값의 정수부분과 같다 X 모든 사분면
    for x in range(1, r1):   #r1 안의 모든 정수 좌표 구하는 for 문
        answer-=4*(((r1**2-x**2)**0.5)//1)  
        #r1 한 x좌표에 존재하는 정수 좌표의 개수는
        #그 x좌표에 대한 원의 y좌표 값의 정수부분과 같다 X 모든 사분면
        if ((r1**2-x**2)**0.5)%1==0:  #r1 원 테두리에 있는 좌표 개수 만큼 더하기
            answer+=4
    answer+=4*r2+1  #r2 x축과 y축 그리고 원점 각 방향마다 반지름 만큼 존재
    answer-=4*r1+1  #r1 x축과 y축 그리고 원점 각 방향마다 반지름 만큼 존재
    answer+=4   #r1 작은 원 테두리 xy축
    return answer

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,   
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    answer = ''
    num_str_li = []    #문자열로 바꾸기 위한 리스트 초기화
    num_len= len(numbers)
    for i in range(0, num_len):
        #02-2 p.18 format, 02-3 p.11 append
        num_str_li.append("{}".format(numbers[i])) 
        #format 함수로 기존 리스트의 요소들을 문자열로 바꿔 준 뒤
        #선언 해놓은 num_str_li에 append를 이용해 요소 삽입
    for i in range(num_len-1):
        for j in range(num_len-1-i):    
            if (num_str_li[j]+num_str_li[j+1]) < (num_str_li[j+1]+num_str_li[j]): 
                num_str_li[j], num_str_li[j+1] = num_str_li[j+1], num_str_li[j]   
            #두 개의 합을 비교하는 이유는 1000, 100, 10, 1 같이 
            #앞자리는 같고 뒤에 0의 개수가 다른 경우
            #자리 수가 적은 수가 앞에 위치하고 내림차순 정렬을 하기 위함
            #for i문이 한번 돌 때 마다 list의 range중 에서 맨 뒤에는 가장 작은 수 위치
            #for j의 range를 하나 씩 줄여나가며 뒤에 가장 작은 수, 
            #그 다음 작은 수가 자리잡게 되면 내림차순으로 정렬
    answer=''.join(num_str_li)  #리스트를 문자열로 변환
    
    return answer