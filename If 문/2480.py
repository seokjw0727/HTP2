a, b, c = map(int, input().split())

# a, b, c 가 모두 같은 경우
if a == b == c:
    print(10000+a*1000)

# 그게 아니라면, a와b, b와c, c와a 가 각각 서로 같은 경우
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)

# 해당 모든 사실을 부정하는 경우(입력받은 세 정수 모두 같지 아니한 경우) 
else:
    print(100 * max(a,b,c))
    # max() 함수, 파이썬의 기본 함수로서, 입력받은 인수중에서 제일 큰 수를 반환한다.

