'''
Q.

정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

제한 조건
num은 int 범위의 정수입니다.
0은 짝수입니다.

입출력 예

num	return
3	"Odd"
4	"Even"

'''

def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

# 다른 사람의 풀이
def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"
    
# 다른 사람의 풀이 2 = 비트연산자 사용
def evenOrOdd2(num):
    return ["Even", "Odd"][num & 1]
