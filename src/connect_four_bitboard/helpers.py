def int_to_bitboard(n: int, rows = 7, cols = 7) -> list[list[int]]:
    """
    Given an integer, returns a two dimensional bit array in the following format:
    ```
    6 13 20 27 34 41 48
    5 12 19 26 33 40 47
    4 11 18 25 32 39 46
    3 10 17 24 31 38 45
    2  9 16 23 30 37 44
    1  8 15 22 29 36 43
    0  7 14 21 28 35 42
    ```
    where 0 is the right-most bit.
    """
    bitboard = []

    for row in range(rows - 1, -1, -1):
        bit_row = []
        for col in range(0, cols):
            # Calculate the index of the bit based on the configuration
            index = col * 7 + row

            # Determine whether the specific bit is set or not set
            bit = n & (1 << index)

            bit_row.append(0 if bit == 0 else 1)
        bitboard.append(bit_row)

    return bitboard

def print_bitboard(n: int, rows = 7, cols = 7):
    """
    Given an integer, prints a bitboard in the following format:
    ```
    .  .  .  .  .  .  .
    5 12 19 26 33 40 47
    4 11 18 25 32 39 46
    3 10 17 24 31 38 45
    2  9 16 23 30 37 44
    1  8 15 22 29 36 43
    0  7 14 21 28 35 42
    ```
    where 0 is the right-most bit.

    The top sentinel row is displayed as dots (`.`).
    """
    bitboard = int_to_bitboard(n, rows, cols)
    print('. ' * cols)
    for row in bitboard[1:]:
        for bit in row:
            print(bit, end=' ')
        print()

if __name__ == '__main__':
    while True:
        n = int(input('> '), 2)
        print_bitboard(n)
