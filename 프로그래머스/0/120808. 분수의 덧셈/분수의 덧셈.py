
def Euclidean(sum1, sum2):
    while sum2 != 0:
        [sum1, sum2] = [sum2, sum1%sum2]
    return sum1


def solution(numer1, denom1, numer2, denom2):
    answer = []
    sum1 = (numer1 * denom2) + (numer2 * denom1)
    sum2 = denom1 * denom2
    sum3 = Euclidean(sum1,sum2)
    if sum3 != 0:
        sum1 = sum1/sum3
        sum2 = sum2/sum3
    else:
        pass
        
    sum1 = int(sum1)
    sum2 = int(sum2)
    answer = [sum1,sum2]
    return answer

def solve():
    numer1 = 1
    denom1 = 2
    numer2 = 3
    denom2 = 4
    answer = solution(numer1, denom1, numer2, denom2)
    print(answer)
    return

solve()