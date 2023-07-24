scores = []
for i in range(5):
    score = int(input("Enter your score: "))
    scores.append(score)
average = sum(scores) / len(scores)
print(f"Scores average: {average}")