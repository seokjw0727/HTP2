
quiz_result= int(input())

for i in range(quiz_result): # 퀴즈 결과값 만큼
    Count_of_O = 0
    Total = 0
    OX = input()
    for s in OX: # OX 만큼 반복하기
        if s == 'O':
            Count_of_O += 1 # O가 있으면 1 추가하기
        elif s == 'X':
            Count_of_O = 0 # 그게 아니라 X가 있으면 0 으로 설정하기
        Total += Count_of_O # Total 에 변수값 Count_of_O 추가하기
    print(Total)
    