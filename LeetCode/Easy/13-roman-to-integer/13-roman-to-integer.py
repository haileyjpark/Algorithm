class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I' : 1, 'V' : 5, 'X':10, 'L':50, 
                 'C' : 100, 'D' : 500, 'M' : 1000}
        answer = 0
        for i in range(0,len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                answer -= roman[s[i]]
            else:
                answer += roman[s[i]]
        return answer + roman[s[-1]]
    
# 다른 사람의 풀이
# Time: 73 ms (44.07%), Space: 14 MB (37.80%) - LeetHub
def romanToInt2(self, s: str) -> int:
	res, prev = 0, 0
	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	for i in s[::-1]:          # rev the s
		if dict[i] >= prev:
			res += dict[i]     # sum the value iff previous value same or more
		else:
			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
		prev = dict[i]
	return res
