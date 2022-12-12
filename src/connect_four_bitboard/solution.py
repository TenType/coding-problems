def solution(bitboard: int) -> bool:
    # Horizontal -
    x = bitboard & (bitboard >> 7)
    if x & (x >> 2 * 7):
        return True

    # Vertical |
    x = bitboard & (bitboard >> 1)
    if x & (x >> 2 * 1):
        return True

    # Ascending diagonal /
    x = bitboard & (bitboard >> 8)
    if x & (x >> 2 * 8):
        return True

    # Descending diagonal \
    x = bitboard & (bitboard >> 6)
    return x & (x >> 2 * 6)
