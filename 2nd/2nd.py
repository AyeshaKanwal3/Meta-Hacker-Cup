# Function to calculate the minimum number of operations needed for a single test case
def calculate(A, B, cost):
    if A <= B / 2:
        # If A is less than or equal to half of B, we can keep buying A to minimize cost
        k = cost / A
        return int(k)
    elif B <= A / 2 or B == A:
        # If B is less than or equal to half of A, or if B equals A, we can keep buying B to minimize cost
        k = (cost / B) * 2 - 1
        return int(k)
    else:
        # If none of the above conditions are met, we need to find an optimal strategy
        k = 0
        while cost > 0:
            if cost < A and cost < B:
                return int(k)
            r = (cost % B)  # Calculate the remainder when cost is divided by B
            k += (cost / B) * 2 - 1  # Buy as many B as possible and subtract one operation (pour) for each purchase
            cost = r
            if cost > 0:
                k += cost / A  # Buy A and increment operations
                cost = cost / A
        return int(k)

# Open the input file for reading
with open("input.txt", "r") as file:
    # Read the number of test cases from the file
    test_cases = int(file.readline())
    
    # Iterate through each test case
    for i in range(test_cases):
        # Read the parameters for the current test case
        A, B, cost = map(int, file.readline().split())
        
        # Calculate the result for the current test case
        result = calculate(A, B, cost)
        
        # Print the result in the required format
        print(f"Case #{i + 1}: {result}")
