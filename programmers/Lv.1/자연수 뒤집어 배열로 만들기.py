'''
Q.

자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

입출력 예
n	       return
12345	[5,4,3,2,1]

'''

def solution(n):
    return list(map(int, str(n)[::-1]))


# 다른 사람의 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))

# 다른 사람의 풀이2
def digit_reverse2(n):
    return [int(i) for i in str(n)][::-1]