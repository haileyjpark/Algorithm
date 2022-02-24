'''
Q.

정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.

입출력 예
n	return
12	28
5	6

입출력 예 설명

입출력 예 #1
12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

입출력 예 #2
5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.
'''

def solution(n):
    divisor_list = []
    for i in range(1,n+1):
        if n % i == 0:
            divisor_list.append(i)
    return sum(divisor_list)


# 다른 사람의 풀이
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])


# 다른 사람의 풀이2
import math
def solution2(n): 
    if n == 0:
        return 0
    
    answer = 0
    
    for i in range(1, int(math.sqrt(n))+1):
    	# 약수일 때
        if n % i == 0:
        	# i가 정수 제곱근일 때
            if i == int(math.sqrt(n)) and math.sqrt(n) == int(math.sqrt(n)):
                answer += int(math.sqrt(n))
                continue
            # i가 정수 제곱근을 아니나 약수 1개를 가질 때
            answer += i + (n // i)
        
    return answer
