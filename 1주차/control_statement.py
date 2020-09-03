### 제어문 

## for문을 이용해서 1부터 100까지의 수를 더하고 출력하라.

# 초기값 
sum=0
for i in range(100): # 0~99 반복
    sum+=i+1 # 1~100의 합
# 출력
print(sum)

## while문을 이용해서 1부터 100까지의 수를 더하고 출력하라.

# 초기값
sum=0
i=1

while(True): 
    sum +=i
    if i==100:
        break
    i+=1
    
# 출력
print(sum)

## 1부터 100까지 3의 배수만 더하고 출력하라.

# 초기값
sum=0

for i in range(100):
    if (i+1) % 3 == 0: # 3의 배수는 3으로 나눴을 때 나머지가 0이다. 
        sum += i+1
# 출력
print(sum)

## A학급에는 10명의 학생이 있고, 이 학생들의 중간고사 점수는 다음과 같다. [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]. for문을 사용해서 A학급의 평균 점수를 구하고 출력하라.

# 초기값
sum=0
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for i in range(len(score)):
    sum += score[i]

avg = round(sum / len(score),2)

# 출력
print('평균 점수는', avg, '입니다.')

## 다음과 같은 리스트가 있다. [1, 3, 5, 40, 90, 100, 2020]. for문을 사용해서 홀수에만 2를 곱하고 리스트를 출력하라.

lsV5 = [1, 3, 5, 40, 90, 100, 2020]
ls = [] # list형 공간 생성 
for i in lsV5:
    if i % 2 == 1: # 홀수일 경우
        i *= 2  # 2를 곱함
    ls.append(i) # 하나씩 ls 변수에 추가 

# 출력
print(ls)


## for문을 이용해 별찍기를  출력하라

length = 5 # 길이
for i in range(length):
    print('*'*(i+1)) # length만큼 별찍기 
