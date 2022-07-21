# FizzBuzz (no modulo)
Play the classic game of FizzBuzz... without the modulo operator!

Given an integer `n`, return a string array with integers (as strings) 1 to `n`, with the following conditions:
- If a number is a multiple of 3, it should have `'Fizz'` instead of the number.
- If a number is a multiple of 5, it should have `'Buzz'` instead of the number.
- If a number is both a multiple of 3 and 5, it should have `'FizzBuzz'` instead of the number.

The modulo (remainder) operator may not be used in the solution.

**Challenge:** Complete this problem *without* using any conditional logic, such as `if/else` statements or the like!

## Example
### Input
```py
n = 15
```

### Output
```py
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

### Explanation
- `1`, `2`, `4`, `7`, `8`, `11`, `13`, and `14` are not multiples of 3 or 5, so they are left as is.
- `3`, `6`, `9`, and `12` are multiples of 3 but not 5, so they have the string `Fizz`.
- `5` and `10` are multiples of 5 but not 3, so they have the string `Buzz`.
- `15` is both a multiple of 3 and 5, so it should have the string `FizzBuzz`.

## Prototype
```py
def solution(n: int) -> list[str]:
    ...
```

## Constraints
- `0 <= n <= 100`
