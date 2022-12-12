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
    # Convert to a string of bits (without the '0b' prefix)
    bitstring = bin(n)[2:]

    # Add padding
    padding = rows * cols - len(bitstring)
    bitstring = '0' * padding + bitstring

    # Append rows
    bitboard = []
    for i in range(rows * (cols - 1), rows * cols):
        row = bitstring[i:0:-cols]
        bitboard.append([int(bit) for bit in row])

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
