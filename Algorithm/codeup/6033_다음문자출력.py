# 30 보다 작은 정수 1개가 입력된다. (1 ~ 29)
# 1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
# 3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.

# 힌트
# 1. n을 입력받는다.
# 2. for을 이용해 i에 1부터 n까지의 값을 넣는다.
# 3. i에 10을 나눈 나머지가 3, 6, 또는 9라면 X 출력, 아니면 i를 출력한다(끝에 end=' '로 공백도 출력해야 됩니다).

n = int(input())

for i in range(1,n+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9: 
        print("X", end=" ")
    else: print(i, end=" ")