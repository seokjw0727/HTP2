n = int(input())  # 과목 수
test_list = list(map(int, input().split())) # 과목 점수
max_score = max(test_list) # 제일 높은 점수

new_list = []
for score in test_list : # score 를 test_lit(과목 점수) 만큼 반복함
    new_list.append(score/max_score *100)  # 새로운 점수 생성, 스코어를 최대 점수로 나눈값 .
test_avg = sum(new_list)/n # new_list 를 n(과목 수) 로 나눔
print(test_avg)


