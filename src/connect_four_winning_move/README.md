# Connect Four Winning Move
In a game of [Connect Four](https://en.wikipedia.org/wiki/Connect_Four), given a two-dimensional array `board` and an integer `col`, determine whether or not the last piece dropped in `board[?][col]` is a winning move and ends the game by forming a horizontal, vertical, or diagonal line of four of the same pieces in a row.

<details>
    <summary><b>How to Play Connect Four</b></summary>
    <b>Connect Four</b> is a two player game where players choose a color and alternate turns by dropping one of their pieces into a 6x7 (row x column) board.<br>
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own pieces.
</details>

## Input
- `board` - A 6x7 (row x column) two-dimensional integer array representing the current state of the Connect Four game, with integers of either `0` (empty), `1` (player one), and `2` (player two)
- `col` - An integer index of a column in `board`

## Output
A boolean value of `True` if the given move is a winning move or `False` if it is not a winning move.

## Example
### Input
```py
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]
col = 3
```

### Output
```py
True
```

### Explanation
- The `col` given is `3`, and the last piece dropped into that column is located at row `2`.
- The piece has the integer `1`, so it belongs to player one.
- Since the piece forms a line of four vertically downwards, and the pieces in the line all belong to player one, the given piece is a winning move, so the output is `True`.

## Prototype
```py
def solution(board: list[list[int]], col: int) -> bool:
    ...
```

## Constraints
- `len(board) == 6`
- `len(board[row]) == 7`
- `0 <= board[row][col] <= 2`
- `board[-1][col] != 0`
- `0 <= col <= 6`

## Hints
<details>
    <summary><b>Optimization Hint</b></summary>
    Although this problem can be completed by using just <code>board</code>, the optimal solution requires using <code>col</code> as well to reduce the amount of pieces that need to be checked.
</details>
