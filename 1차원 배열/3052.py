# for i in range(10):
#     A = int(input())



arr = [] # list 변수를 하나 만든다.

for i in range(10):
    n = int(input())
    arr.append(n % 42) # arr 이라는 list 변수에 입력받은 정수를 42로 나눈 나머지를 추가한다.
arr = set(arr) # arr 이라는 list 변수에서 중복되지 아니한 unique 원소를 얻음
print(len(arr)) # len 함수를 통해서 설정한 arr 변수의 길이를 출력한다.