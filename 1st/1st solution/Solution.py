# Read input from an input file
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    T = int(input_file.readline().strip())  # Read the number of test cases from the first line of the input file.

    # Process each test case
    for i in range(1, T + 1):
        S, D, K = map(int, input_file.readline().strip().split())  # Read S, D, and K values from each line of the input file.
        
        # Calculate the total number of ingredients
        total_buns = S * 4 + D * 2
        total_patties = S + D * 2
        total_cheese = S + D * 2

        # Check if there are enough ingredients to build a K-decker cheeseburger
        if total_buns >= K * 2 and total_patties >= K and total_cheese >= K:
            result = "YES"  # There are enough ingredients to build a K-decker cheeseburger.
        else:
            result = "NO"   # There are not enough ingredients to build a K-decker cheeseburger.
        
        # Write the result to the output file
        output_file.write(f"Case #{i}: {result}\n")  # Write the result to the output file in the specified format.

# Print a message indicating that the output has been written
print("Output has been written to 'output.txt'.")
