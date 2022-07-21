def solution(n: int) -> list[str]:
    result = [str(i) for i in range(1, n + 1)]

    for i in range(2, n, 3):
        result[i] = 'Fizz'

    for i in range(4, n, 5):
        result[i] = 'Buzz'

    for i in range(14, n, 15):
        result[i] = 'FizzBuzz'

    return result
