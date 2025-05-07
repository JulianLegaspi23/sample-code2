import chess
import chess.engine

def play_chess():
    board = chess.Board()
    print("Welcome to Chess!")
    print(board)

    while not board.is_game_over():
        try:
            move = input("Enter your move (e.g., e2e4): ")
            board.push_san(move)
            print("\nYour move:")
            print(board)

            if board.is_game_over():
                break

            print("\nComputer is thinking...")
            with chess.engine.SimpleEngine.popen_uci("/path/to/your/engine") as engine:
                result = engine.play(board, chess.engine.Limit(time=1.0))
                board.push(result.move)
                print("\nComputer's move:")
                print(board)

        except ValueError:
            print("Invalid move. Try again.")

    print("\nGame Over!")
    print("Result:", board.result())

if __name__ == "__main__":
    play_chess()