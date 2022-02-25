'''
해독할 암호

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(1)와 달(0),
Code의 세상 안으로!(En-Coding)

'''


text = ['   + -- + - + -   ',
       '   + --- + - +   ',
       '   + -- + - + -   ',
       '   + - + - + - +   ']
# 첫번째 방법
def secretCode(text):
    return ''.join([chr(int(i.strip().replace(' ','').replace('+', '1').replace('-','0'),2)) for i in text])

# 두번째 방법
def secretCode2(text):
    s = [i.strip().replace(' ','').replace('+', '1').replace('-','0') for i in text]
    return ''.join(list(map(lambda x : chr(int(x,2)),s)))

#세번째 방법
def secretCode3(text):
    s = [i.strip().replace(' ','').replace('+', '1').replace('-','0') for i in text]
    def f(x):
        return chr(int(x,2))
    list(map(f,s))
    
    