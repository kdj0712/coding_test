def solution(price):
    answer = 0
    if 100000> price > 0:
        answer = (price)*1
    elif 300000 > price >= 100000:
        answer = (price)*0.95
        answer = int(answer)
    elif 500000 > price >= 300000:
        answer = (price)*0.9
        answer = int(answer)
    elif price >= 500000:
        answer = (price)*0.8
        answer = int(answer)
    return answer

def solve():
    price = 500000
    answer = solution(price)
    print("{}".format(answer))
    return

solve()