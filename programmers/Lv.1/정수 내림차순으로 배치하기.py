'''
Q.

함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
n은 1이상 8000000000 이하인 자연수입니다.

입출력 예
n	    return
118372	873211

'''

# 첫번째 풀이
def solution(n):
    n_list = list(str(n))
    n_list.sort(reverse=True)
    return int(''.join(n_list))
# 이 풀이에서는 3개의 테스트에 런타임 에러가 발생했다.

# 수정한 풀이
def solution2(n):
    n_list = list(str(int(n)))
    n_list.sort(reverse = True)
    return int("".join(n_list))


# 다른 사람의 풀이
def solution3(n):
    return int(''.join(sorted(str(n), reverse = True)))
