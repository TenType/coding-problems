def solution(board: list[list[int]], col: int) -> bool:
    # Find row and piece
    row = 0
    while board[row][col] == 0:
        row += 1
    piece = board[row][col]

    row_len = len(board)
    col_len = len(board[row])

    # Horizontal, vertical, and diagonal checks
    for (run, rise) in ((1, 0), (0, 1), (1, -1), (1, 1)):
        length = 1

        # Check positive and negative directions
        for direction in (1, -1):
            # The last piece in a vertical win is always on top
            if run == 0 and direction == -1:
                continue

            for step in range(1, 4):
                row_check = row + rise * step * direction
                col_check = col + run * step * direction

                # Out of bounds or not matching
                if (row_check < 0 or row_check >= row_len
                    or col_check < 0 or col_check >= col_len
                    or board[row_check][col_check] != piece):
                    break

                length += 1

                # Four in a row
                if length == 4:
                    return True

    return False
