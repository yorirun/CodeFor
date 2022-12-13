import random
'''난수로 만드는 일라이저 알고리즘 --> 일라이저알고리즘 = 랜덤값 반복'''



a = input("당신은 누구인가요?\n 이름만 입력\n")
print( a + "님 안녕하세요!\n 지금은 무엇을 말하고싶은가요?")


print("\n 필요한 것의 번호를 입력해주세요!\n")
b = int(input("1.무엇이 필요하다\n"
                 "2.상태가 이렇다\n"))

if b == 1:



 num1 = random.randint(1, 2)
 #print(f'{num1}')
if num1 == 1:
 print("왜 필요한가요?")
 d = input("\n")
print("그렇군요..")

if num1 == 2:
 print(" 정말 도움이될까요?")
d = input("\n")
print("네, 알겠습니다.")

if b ==2:


    num2 = random.randrange(5, 6)

    if num2 == 5:
        print("왜 필요한가요?")
d = input("\n")
print("그렇군요..")

if num2 == 6:
 print(" 정말 도움이될까요?")
d = input("\n")
print("네, 알겠습니다.")

'''현재까지 찾은 오류 -> 랜덤값은 나오지만 랜덤값에 상관없이 모든 값이 출력되는 오류가 있음'''
