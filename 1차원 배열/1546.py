how_much = int(input())
scores = []

for i in range(how_much):
    score = int(input())
    scores.append(score)
print(f"{scores / how_much}")