def solution(my_string,num1,num2):
    a = my_string[num1]
    b = my_string[num2]
    answers = []
    for i in range(len(my_string)):
        if i == num1:
            answers.append(b)
        elif i == num2:
            answers.append(a)
        else:
            answers.append(my_string[i])
    answer = ''.join(map(str,answers))
    return answer

def solve():
    my_string = "hello"
    num1 = 1
    num2 = 2
    answer = solution(my_string,num1,num2)
    print("{}".format(answer))
    return

solve()