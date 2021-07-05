'''
2021. 06. 29
Woody
Python Programming
'''


#Print (In order to see the result more clearly, add '\n')
print("#print\n")
print("Hello")                              #Hello
print("World")                              #World
print("Hello World")                        #Hello World
print("Hello", "World\n")                   #Hello World

print("HelloWorld")                         #HelloWorld
print("Hello", "World", sep='')             #HelloWorld
print("He", "llo", "Wor", "ld")             #He llo Wor ld
print("He", "llo", " Wor", "ld\n", sep='')  #Hello World (일부러 W앞에 한칸 공백)

print("Hello", end=' ')                     
print("World")                              #Hello World (한 줄에 print)
print("Hello", end=' ')
print("\nWorld")                            #Hello 한 줄 띄고 World


print("\n", "-"*30, "\n")


#binary, decimal, hexadecimal
print("#number\n")
num10 = 10          #10진수 10
num16 = 0xa         #16진수 10
num2 = 0b1010       #2진수  10

print(num10, num16, num2)
print(num10, num16, num2, sep="\n")


print("\n", "-"*30, "\n")


#operator
print("#operator\n")
a = 10                                      #a라는 변수에 10 저장
b = 3                                       #b라는 변수에 3 저장
print(a + b)                                #덧셈
print(a - b)                                #뺄셈
print(a * b)                                #곱셈
print(a ** b)                               #거듭제곱 (10의 3제곱)
print(a / b)                                #나눗셈
print(round(a / b))                         #반올림
print(round(a / b, 2))                      #소수점둘째자리까지 반올림
print(a // b)                               #몫
print(a % b)                                #나머지
