def solution(babbling):
    def generate_combinations(possibles, max_length):
        def recurse(current, remaining, results):
            if 0 < len(current) <= max_length:
                results.add(''.join(current))  
                results.add(''.join(current[::-1]))  
            if len(current) == max_length or not remaining:
                return
            for i in range(len(remaining)):
                next_chars = current + [remaining[i]]
                recurse(next_chars, remaining[:i] + remaining[i+1:], results)
        results = set()
        recurse([], possibles, results)
        return list(results)
    possibles = ["aya", "ye", "woo", "ma" ]
    answer = 0
    combinations = generate_combinations(possibles, 4)
    for x in range(len(babbling)):
        if babbling[x] in combinations:
            answer = answer + 1
        else:
            pass
    return answer