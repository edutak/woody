'''
2021. 06. 30
Woody
Python Programming
'''

'''
1. oper_num 이라는 변수에 1부터 10사이의 랜덤값을 추출하여 대입한다.
'''
import random
oper_num = random.randint(1,10)



'''
2. 추출된 값이 1이거나 6이면 300 과 50 의 덧셈 연산을 처리한다.
   추출된 값이 2이거나 7이면 300 과 50 의 뺄셈 연산을 처리한다.
   추출된 값이 3이거나 8이면 300 과 50 의 곱센 연산을 처리한다.
   추출된 값이 4이거나 9이면 300 과 50 의 나눗셈 연산을 처리한다.
   추출된 값이 5이거나 10이면 300 과 50 의 나머지 연산을 처리한다.
'''
if oper_num == 1 or oper_num == 6:
    result = 300 + 50
elif oper_num == 2 or oper_num == 7:
    result = 300 - 50
elif oper_num == 3 or oper_num == 8:
    result = 300 * 50
elif oper_num == 4 or oper_num == 9:
    result = 300 / 50
elif oper_num == 5 or oper_num == 10:
    result = 300 % 50


'''
3. 출력 형식(단, 결과를 출력하는 수행문장은 한 번만 구현한다.)
    결과값 : XX
'''
#print(oper_num)                #check
print("결과값 :", result)
