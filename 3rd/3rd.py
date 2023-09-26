def winner(rows, cols, alice_moves, bob_moves):
    is_alice_move = True
    sr, sc = 1, 1

    while sr <= rows and sc <= cols:
        if is_alice_move:
            sr = sr if sr == rows else min(sr + alice_moves, rows)
        else:
            sc = sc if sc == cols else min(sc + bob_moves, cols)

        if sr == rows and sc == cols:
            return "YES" if is_alice_move else "NO"

        is_alice_move = not is_alice_move

    return "YES" if is_alice_move else "NO"


def main():
    with open("input.txt", "r") as input_file:
        T = int(input_file.readline().strip())
        t_count = 1

        with open("output.txt", "w") as output_file:
            while t_count <= T:
                input_params = list(map(int, input_file.readline().strip().split()))
                rows, cols, alice_moves, bob_moves = input_params
                result = winner(rows, cols, alice_moves, bob_moves)
                output_file.write(f"Case #{t_count}: {result}\n")
                t_count += 1


if __name__ == "__main__":
    main()
