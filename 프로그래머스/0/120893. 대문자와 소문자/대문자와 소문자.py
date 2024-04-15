def solution(my_string):
    answers = []
    for x in range(len(my_string)):
        s = my_string[x]
        if  s.isupper() == True:
            small = s.lower()
            answers.append(small)
        elif s.islower() == True:
            big = s.upper()
            answers.append(big)
        else:
            pass
    answer = ''.join(map(str, answers))
    return answer

def solve():
    my_string = "abCdEfghIJ"
    answer = solution(my_string)
    print("{}".format(answer))
    return

solve()