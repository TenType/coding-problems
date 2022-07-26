from solution import solution

def test_no_winner_first_move():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]
    assert not solution(board, 3)

def test_no_winner_almost():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 2, 0],
        [0, 1, 2, 1, 2, 1, 0],
    ]
    assert not solution(board, 3)

def test_no_winner_draw_1():
    board = [
        [2, 2, 2, 1, 1, 1, 2],
        [1, 2, 2, 2, 1, 1, 1],
        [2, 2, 1, 1, 2, 2, 2],
        [1, 1, 2, 2, 2, 1, 2],
        [1, 2, 1, 1, 2, 2, 1],
        [1, 2, 1, 2, 1, 1, 1],
    ]
    for column in range(0, 7):
        assert not solution(board, column)

def test_no_winner_draw_2():
    board = [
        [2, 2, 2, 1, 1, 1, 2],
        [1, 1, 1, 2, 2, 2, 1],
        [2, 2, 2, 1, 1, 2, 2],
        [1, 1, 1, 2, 2, 1, 1],
        [1, 1, 2, 1, 2, 1, 2],
        [2, 2, 1, 2, 1, 1, 2],
    ]
    for column in range(0, 7):
        assert not solution(board, column)

def test_winner_horizontal_left():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
    ]
    for column in range(0, 4):
        assert solution(board, column)

def test_winner_horizontal_right():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1],
    ]
    for column in range(3, 7):
        assert solution(board, column)

def test_winner_horizontal_complex_1():
    board = [
        [1, 2, 2, 2, 1, 0, 1],
        [2, 2, 1, 1, 1, 1, 1],
        [2, 1, 1, 2, 2, 2, 1],
        [1, 2, 2, 1, 1, 1, 2],
        [2, 2, 1, 2, 2, 2, 1],
        [1, 1, 2, 1, 2, 1, 2],
    ]
    assert solution(board, 5)

def test_winner_horizontal_complex_2():
    board = [
        [2, 1, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 1, 2, 2],
        [2, 1, 2, 2, 1, 1, 2],
        [1, 2, 1, 1, 1, 2, 1],
        [2, 1, 2, 2, 2, 1, 1],
        [2, 1, 2, 1, 1, 2, 1],  
    ]
    assert solution(board, 4)

def test_winner_vertical_left():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
    ]
    assert solution(board, 0)

def test_winner_vertical_right():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1],
    ]
    assert solution(board, 6)

def test_winner_vertical_complex_1():
    board = [
        [1, 2, 1, 1, 2, 2, 0],
        [1, 2, 2, 1, 1, 2, 1],
        [2, 1, 2, 1, 2, 1, 1],
        [1, 1, 2, 1, 1, 2, 2],
        [1, 1, 1, 2, 2, 2, 1],
        [2, 2, 2, 1, 2, 2, 1],
    ]
    assert solution(board, 3)

def test_winner_vertical_complex_2():
    board = [
        [2, 1, 0, 2, 1, 1, 0],
        [1, 2, 2, 2, 1, 2, 2],
        [1, 1, 2, 1, 1, 1, 2],
        [2, 1, 2, 1, 2, 2, 1],
        [1, 1, 2, 1, 1, 2, 2],
        [1, 2, 1, 2, 2, 2, 1],
    ]
    assert solution(board, 2)

def test_winner_ascending_diagonal_left():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 2, 0, 0, 0],
        [0, 1, 2, 2, 0, 0, 0],
        [1, 2, 2, 2, 0, 0, 0],
    ]
    for column in range(0, 4):
        assert solution(board, column)

def test_winner_ascending_diagonal_right():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 1, 2, 2],
        [0, 0, 0, 1, 2, 2, 2],
    ]
    for column in range(3, 7):
        assert solution(board, column)

def test_winner_ascending_diagonal_complex_1():
    board = [
        [2, 2, 1, 1, 2, 0, 1],
        [1, 2, 1, 1, 1, 1, 1],
        [1, 1, 2, 2, 1, 2, 2],
        [2, 1, 1, 1, 2, 2, 2],
        [1, 2, 2, 2, 1, 1, 1],
        [2, 2, 1, 1, 2, 2, 2],
    ]
    assert solution(board, 5)

def test_winner_ascending_diagonal_complex_2():
    board = [
        [2, 0, 2, 2, 2, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [2, 0, 1, 1, 2, 0, 2],
        [1, 0, 1, 1, 2, 2, 1],
        [1, 0, 2, 2, 2, 1, 2],
        [1, 0, 1, 2, 1, 2, 2],
    ]
    assert solution(board, 5)

def test_winner_descending_diagonal_left():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0],
        [2, 2, 1, 0, 0, 0, 0],
        [2, 2, 2, 1, 0, 0, 0],
    ]
    for column in range(0, 4):
        assert solution(board, column)

def test_winner_descending_diagonal_right():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 2, 2, 1, 0],
        [0, 0, 0, 2, 2, 2, 1],
    ]
    for column in range(3, 7):
        assert solution(board, column)

def test_winner_descending_diagonal_complex_1():
    board = [
        [1, 2, 2, 1, 0, 1, 2],
        [1, 2, 2, 1, 1, 2, 1],
        [2, 1, 1, 2, 2, 1, 2],
        [2, 2, 2, 1, 1, 2, 1],
        [1, 1, 1, 2, 1, 1, 2],
        [1, 2, 2, 1, 2, 2, 1],
    ]
    assert solution(board, 4)

def test_winner_descending_diagonal_complex_2():
    board = [
        [2, 1, 0, 1, 2, 2, 2],
        [1, 1, 0, 1, 2, 1, 1],
        [1, 2, 2, 1, 1, 2, 2],
        [1, 1, 1, 2, 2, 1, 1],
        [2, 2, 2, 1, 2, 2, 2],
        [1, 1, 1, 2, 1, 2, 2],
    ]
    assert solution(board, 2)
