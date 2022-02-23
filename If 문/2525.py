H, M = map(int, input().split())
timer = int(input()) 

# timer 를 60을 나눈수 
H += timer // 60
M += timer % 60

# 만약에 M이 60보다 크면 H 에다가 1 더하고 M 에서 60을 뺌 (60분이 넘어가면 1시간으로 보기때문에.)
if M >= 60:
    H += 1
    M -= 60

# 만약에 H가 24보다 크면, H에다가 24 빼버림 (하루는 24시간을 넘어가지 아니하니까.)
if H >= 24:
    H -= 24

print(H,M)