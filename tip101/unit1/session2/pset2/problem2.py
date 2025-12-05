def average(scores):
    avg = 0
    for x in range(len(scores)):
        avg = avg + scores[x]
    avg = avg / len(scores)
    return avg
scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)