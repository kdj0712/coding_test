def solution(my_string, n):
    
    i = len(my_string)
    answer = []
    for i in range(len(my_string)):
        answer.append((my_string[i])*(n))
    answer =''.join(map(str, answer))
    return answer

def solve():
    my_string = "hello"
    n = 3
    answer = solution(my_string, n)
    print(answer)
    return

solve()