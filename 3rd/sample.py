def winner(rows, cols, alice_moves, bob_moves):
    is_alice_move = True
    sr, sc = 1, 1

    while sr <= rows and sc <= cols:
        if is_alice_move:
            sr = min(rows, sr + alice_moves)
        else:
            sc = min(cols, sc + bob_moves)

        if sr == rows and sc == cols:
            if is_alice_move:
                return "YES"
            else:
                return "NO"

        is_alice_move = not is_alice_move

    return "YES" if is_alice_move else "NO"

# Function to read input from the input file and return a list of test cases
def read_input(input_file):
    test_cases = []
    T = int(input_file.readline().strip())
    
    for _ in range(T):
        rows, cols, alice_moves, bob_moves = map(int, input_file.readline().strip().split())
        test_cases.append((rows, cols, alice_moves, bob_moves))
    
    return test_cases

# Function to write the results to the output file
def write_output(output_file, results):
    for result in results:
        output_file.write(f"{result}\n")

# Read input from the input file
with open('input.txt', 'r') as input_file:
    test_cases = read_input(input_file)
    results = []

    # Process each test case
    for test_case in test_cases:
        result = winner(*test_case)
        results.append(result)

    # Open the output file for writing
    with open('output.txt', 'w') as output_file:
        write_output(output_file, results)

print("Output has been written to 'output.txt'.")
