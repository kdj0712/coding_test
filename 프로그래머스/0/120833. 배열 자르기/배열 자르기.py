def solution(numbers,num1,num2):
    answer=[]
    for i in range(num1,(num2+1)):
        answer.append(numbers[i])
    return answer

def solve():
    numbers = [1, 2, 3, 4, 5 , 6 , 7 , 8 , 9 , 10 ]
    num1 = 3
    num2 = 8
    answer = solution(numbers,num1,num2)
    print("{}".format(answer))
    return

solve()