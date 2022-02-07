'''
Q.

인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

Fibonacci 순열은 아래와 같이 정의됩니다.
F0 = 0
F1 = 1
Fn = Fn - 1 + Fn - 2, n >= 2

재귀함수 작성 연습을 의도한 것이므로, 재귀적 방법으로도 프로그래밍해 보고, 반복적 방법으로도 프로그래밍해 보시기 바랍니다.

'''

# 재귀 함수
def solution(x):
    if(x < 2): return x

    answer = solution(x-1) + solution(x-2)
    return answer

# 반복문 함수
def solution2(x):
    if x <= 1:
        return x
    n, m = 1, 1
    for i in range(1,x):
        n,m = m, n+m

    return n