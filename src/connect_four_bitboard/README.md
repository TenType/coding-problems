# Connect Four Bitboard
Given a player's [Connect Four](https://en.wikipedia.org/wiki/Connect_Four) bitboard, determine whether or not there are any `1` bits that forms a horizontal, vertical, or diagonal line in a row.

<details>
    <summary><b>How to Play Connect Four</b></summary>
    <b>Connect Four</b> is a two player game where players choose a color and alternate turns by dropping one of their pieces into a 6x7 (row x column) board.<br>
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own pieces.
</details>

## Input
`bitboard` - A 64-bit unsigned integer representing this 7x7 bitboard configuration:
```
.  .  .  .  .  .  .
5 12 19 26 33 40 47
4 11 18 25 32 39 46
3 10 17 24 31 38 45
2  9 16 23 30 37 44
1  8 15 22 29 36 43
0  7 14 21 28 35 42
```
0 is the right-most bit, while 48 is the left-most bit.

For convenience, there is an extra sentinel row (all 0s) at the top of the bitboard. This corresponds to every 7th bit and denotes the separation of columns.

## Output
`True` if there is a line of `1` bits that forms a horizontal, vertical, or diagonal line in a row or `False` otherwise.

## Example
### Input
```py
0b0000000_0000100_0000110_0001010_0000011_0000011_0000000
```
(represented as the integer `139070587264`)

### Output
```py
True
```

### Explanation
The integer corresponds to the following bitboard:
```
. . . . . . .
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 0 0 1 1 0
0 1 1 1 1 0 0
0 1 1 0 0 0 0
```
Since the bitboard contains a horizontal line of four `1` bits in the second to bottom row, the output is `True`.

## Prototype
```py
def solution(bitboard: int) -> bool:
    ...
```

## Constraints
- `0 <= bitboard < 2^64`
- `bitboard & 0b_1000000_1000000_1000000_1000000_1000000_1000000_1000000 == 0` (Every 7th bit is guaranteed to be `0`.)

## Helpers
The following helper functions are defined in `helpers.py` for **only** debugging purposes:
- `int_to_bitboard()` - Converts an integer into a two dimensional array of bits.
- `print_bitboard()` - Prints an integer as a bitboard.

