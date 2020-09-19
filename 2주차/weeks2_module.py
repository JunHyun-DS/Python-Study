import random
import datetime

## 로또 번호 생성기 함수 만들기. 정렬까지 포함할 것.

def lotto():
    lotto_v = random.sample(range(0, 46), 6) # 0~45 randomsampling
    lotto_v = sorted(lotto_v, reverse=False) # 정렬

    print('output: ', lotto_v, sep='')

## 다음과 같은 계산기 코드가 있을 때, 상세하게 살을 덧붙이고, 예외처리와 모듈화를 진행하라.

def cal():
    while 1:
        try:
            a = int(input())  # 숫자1 입력부
            if a == 0:
                print('계산기가 종료되었습니다.')
                break
                
            b = input()  # 연산자 입력부
            c = int(input())  # 숫자2 입력부
            if b == "+":
                print(a, "+", c, "=", a + c)
            elif b == "-":
                print(a, "-", c, "=", a - c)
            elif b == "*":
                print(a, "*", c, "=", a * c)
            elif b == "/":
                print(a, "*", c, "=", a / c)
            else:
                print('연산자를 재확인해주세요\n처음부터 다시입력해주세요\n')  # 문자열 예외처리
                continue

        # 예외처리
        except ZeroDivisionError as e:
            print(e)
        except ValueError as f:
            print(f)

if __name__ == "__main__":
    cal()    

## 다음과 같이 문자열을 분석하는 함수를 만들어라. 내장함수를 이용하라

def str_analysis(string):
    inp = string
    inp_length = len(inp)
    descending = sorted(inp, reverse=True)   # 문자의 내림차순 정렬
    big_str = descending[0] # 정렬 후 가장 큰 변수
    rev = inp[::-1] # 전체 데이터를 역순으로 가져오기

    # 출력
    print('문자의 개수: ', inp_length, sep='')
    print('가장 큰 문자열: ', big_str, sep='')
    print('뒤집은 문자열: ', rev, sep='')

## 내장함수와 datetime라이브러리를 이용하여 지금을 출력하고, 49일 1시간 8분 7초 후가 언제인지 출력하는 함수를 만드시오.

def time(days=0, hours=0, minutes=0, seconds=0):
    now = datetime.datetime.now()  # 현재 시간
    future = datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    result = now + future  # 미래 시간

    print('현재: ', now.year, '년 ', now.month, '월 ', now.day, '일 ', now.hour, '시 ', now.minute, '분 ', now.second, '초',
          sep='')
    print('미래: ', result.year, '년 ', result.month, '월 ', result.day, '일 ', result.hour, '시 ', result.minute, '분 ',
          result.second, '초', sep='')

## 영한사전 프로그램을 만들어라. 딕셔너리를 이용할 것, 모듈화/예외처리 할 것

# 문자는 컴퓨터가 항상 인식을 하기 때문에 try except를 사용하지 않고 조건문을 이용해서 예외처리를 했음
def word(): # 단어
    words = {'apple': '사과', 'banana': '바나나', 'camel': '낙타'}

    return(words)

def dictionary(): # 사전
    words = word()
    words = dict(words)

    input_words = input('영어로검색\n한글로검색\n전체출력\n\n') # 첫 단어 입력
    input_words = input_words.strip() # 한글로 입력할시 공백 떄문에 오류가 자주 떠서 공백 제거

    # 영한사전
    if input_words == '영어로검색':
        input_words = input('단어를 입력하세요: ')
        input_words = input_words.strip()

        if input_words not in words.keys():
            print('-삐빅-') # 예외처리

        for key, value in words.items():
            if key == input_words: # 영한사전
                print(key, ': ', value, sep='')

    # 한영사전
    elif input_words == '한글로검색':
        input_words = input('단어를 입력하세요: ')
        input_words = input_words.strip()

        if input_words not in words.values():
            print('-삐빅-') # 예외처리

        for key, value in words.items():
            if value == input_words: # 한영사전
                print(value, ': ', key, sep='')

    # 전체 출력
    elif input_words == '전체출력':
        for key, value in words.items(): # word의 있는 key, value값을 하나씩 출력
            print(key, ': ', value, sep='')

    else:
        print('-삐빅-') # 예외처리
