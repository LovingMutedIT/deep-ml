import math

def softmax(scores: list[float]) -> list[float]:
    sum = 0
    for i in range(len(scores)):
        sum += round(pow(math.e, scores[i]), 4)
    
    for i in range(len(scores)):
        scores[i] = round(round(pow(math.e, scores[i]), 4) / sum, 4)

    return scores