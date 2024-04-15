def solution(num_list, n):
    answer = []
    z = 0
    y = len(num_list)/n
    y = int(y)
    for x in range(y):
        answer.append(num_list[z:z+n])
        z = z + n
    return answer