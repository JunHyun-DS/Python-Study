### 함수와 입출력

## 학점산출함수를 만들어라. 학생의 점수를 입력할 수 있고, 점수를 기반으로 학점을 매겨주고 출력해야한다.

def prt(score):
    prt = ''
    if score >= 80:
        prt= 'output : A'
    elif score >=50:
        prt = 'output : B'
    elif score >=30:
        prt = 'output : C'
    else:
        prt = 'output : F'

    return(prt)

score = int(input('점수를 입력하세요: ')) # input함수는 string을 뱉기 때문에 int를 씌워줘야 한다.
prt = prt(score)

# 출력 
print('input :',score)
print(prt)

## 짝수 판별 프로그램을 만들어라. 수를 하나 입력할 수 있고, 그 수가 짝수이면 True, 홀수이면 False를 리턴한다.

def oddEven(num):
    if num % 2 ==0:
        print('return : True')
    else:
        print('return : False')

num = int(input('수를 입력하세요: '))

print('input :',num)
oddEven(num)

## 주민등록번호 판별 프로그램을 만들어라. 주민등록번호를 입력할 수 있고, 그 번호를 통해 몇년생인지, 그리고 남자 인지 여자인지를 판별하고 출력해야한다.

# 홀수면 남자, 짝수면 여자
def bg_print(second):
    second = int(second[0])  # 주민등록번호 뒷자리 중 첫번째 자리
    if second % 2 == 1:
        print(', 남자')
    else:
        print(', 여자')

resident_num = input('주민등록번호를 입력해주세요(- 포함) : ')
first, second = resident_num.split('-') # 주민등록번호 앞자리 뒷자리 나누기

print('input :', resident_num) # 출력
print('output : ', first[0:2], '년생', end='', sep='')
bg_print(second) # 남/여 출력

## 간단한 계산기 함수를 만들어라. 사칙연산과 나머지 연산이 되어야한다.

# 계산함수
def calculate():
    num = 0
    first = int(input('수를 입력하세요: '))
    num2 = first
    inp = []  # list형으로 받을 숫자
    oper = []  # list형으로 받을 연산자

    while(True):

        operator = input('연산을 입력하세요 (+,-,*,/), \n종료하려면 quit을 누르세요: ')
        if operator == 'quit':
            break
        second = int(input('다음 수를 입력하세요: '))

        if operator == '+':
            num = num2 + second
        elif operator == '-':
            num = num2 - second
        elif operator == '*':
            num = num2 * second
        elif operator == '/':
            if second == 0:
                print('\nZeroDivisionError\n')
                break
            else:
                num2 = first / second
        num2 = num

        inp.append(second)
        oper.append(operator)

    return(first, inp, oper, num)

# 식의 표현함수
def express(inp, oper, first):
    express = [first]
    for i in range(len(inp)): # 식을 express라는 변수에 대입
        express.append(oper[i])
        express.append(inp[i])

    express = map(str, express) # int, string형이 섞여있어서 안에있는 데이터를 문자열로 형변환
    express = ' '.join(express) # list(문자열)를 str형으로 표현
    return(express)

# 출력함수
def prt(express, num):
    print('input: ', express, sep='')
    print('output: ', num, sep='')

cal = list(calculate())
first = cal[0] # 첫 숫자
inp = cal[1] # 계산할 숫자
oper = cal[2] # 연산자
output = cal[3] # 결과

# 식의 표현
exp = express(inp, oper, first)

# 출력
prt(exp, output)

## 거스름돈 함수를 만들어라. 금액을 입력하면 거스름돈을 출력해야한다.

price = [1000, 500, 100, 50, 10]
change_ls = [5000, 1000, 500, 100, 50, 10]

# 시작함수
def start():
    select = 0 # 선택 물품 초기값
    sum = 0  # 돈 합계 초기값
    num_ls = [0, 0, 0, 0, 0]  # 개수 list형태로 받기

    # 메뉴판 보여주기
    print(0, '. 종료', sep='')
    for i in range(len(price)):
        print(i + 1, '. ', price[i], '원', sep='')

    while True:
        hello = int(input('물품을 선택해주세요(1,2,3,4,5): '))

        if hello == 0:
            break
        num = int(input('몇개를 선택하시겠습니까? '))

        if hello == 1:
            select = price[0]
            num_ls[0] += num
        elif hello == 2:
            select = price[1]
            num_ls[1] += num
        elif hello == 3:
            select = price[2]
            num_ls[2] += num
        elif hello == 4:
            select = price[3]
            num_ls[3] += num
        elif hello == 5:
            select = price[4]
            num_ls[4] += num
        else:
            continue

    # 돈 입력 받기
    put = int(input('돈을 넣어주세요: '))

    # 금액의 합
    for i in range(len(price)):
        sum += (price[i] * num_ls[i])

    return put, sum, num_ls # 구매한 개수

# 거스름돈 반환 함수
def change(put, sum):
    change_cnt = [0, 0, 0, 0, 0, 0]  # 거스름돈 지페 개수
    change = put - sum  # 거스름돈
    change1 = put - sum  # 출력용 거스름돈

    # 거스름돈 개수 구하기
    for i in range(len(change_ls)):
        change_cnt[i] = (change // change_ls[i]) # 몫
        change -= (change_ls[i]*change_cnt[i]) # 나머지

    return change1, change_cnt

# 출력함수
def prt(put, change_cnt, change1, sum, num_ls):

    
    print('\ninput : ', put, '원', sep='')
    print('price: ', sum, sep='')
    print('output : ', change1, '원', sep='')

    print('\n* 거스름돈 *\n')
    for i in range(len(change_ls)):
        print(change_ls[i], '원: ', change_cnt[i], '개', sep='')

    # 구매물품 출력
    print('\n* 구매물품 가격 *\n')
    for i in range(len(price)):
        print(price[i], '원 : ', sep='', end='')
        print(num_ls[i], '개', sep='')

# 변수 생성
start = start()
put = start[0]
sum = start[1]
num_ls = start[2]
change = change(put, sum)
change1 = change[0]
change_cnt = change[1]

# 출력
prt(put, change_cnt, change1, sum, num_ls)


### 이차방정식의 근을 구하는 함수를 만들어라. 제곱근은 math 라이브러리 활용!

import math

# 1x^2+6*x -27 = 0
def quest():
    coef = [0,0,0]
    coef[0] = input('x^2의 계수를 입력하세요: ')
    coef[1] = input('x의 계수를 입력하세요: ')
    coef[2] = input('y절편의 계수를 입력하세요: ')
    coef = list(map(int, coef))
    return(coef)

# 근의 공식(quadratic formula)
def formula(a,b,c):
    quadratic_formula_plus = (-b + math.sqrt(b**2-4*a*c)) / (2*a)
    quadratic_formula_minus = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    return([quadratic_formula_plus, quadratic_formula_minus])


coef = quest()

x = formula(coef[0], coef[1], coef[2])
print('input : ', coef[0], 'x^2', '+',coef[1], 'x', coef[2], sep='')
print('output : ','x1 = ', x[0], ', x2 = ', x[1], sep='')


