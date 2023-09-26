file_input = "file_input.txt"
from collections import defaultdict

# Create a defaultdict with int as the default factory
target = 0
count = 0
with open(file_input,"r") as file:
    for i, nums in enumerate(file):
        numbers = nums.split()
        num_dict = defaultdict(int)

        if i>0:
            if i%2 ==0:
                count +=1
                if len(numbers)==1:
                    print(f"Case #{count}: {numbers[0]}")
                else:
                    for j in range(len(numbers)):
                        for k in range(j+1,len(numbers)):
                            num_dict[int(numbers[j])+int(numbers[k])] +=1
                    
                    max_occurrences = max(num_dict.values())
                    # Find the smallest number with maximum occurrences
                    min_num = min(num for num, occurrences in num_dict.items() if occurrences == max_occurrences)

                    integer_list = [int(x) for x in numbers]

                    j = 0
                    while j < len(integer_list):
                        k = j + 1
                        while k < len(integer_list):
                            if integer_list[j] + integer_list[k] == min_num:
                                del integer_list[j]
                                del integer_list[k - 1]
                                j = 0  # Reset j to 0 after deletion
                                break
                            k += 1
                        else:
                            j += 1


                    if len(integer_list)==1 and integer_list[0] !=min_num:
                        target = min_num-integer_list[0]
                        print(f"Case #{count}: {target}")
                    else:
                        print(f"Case #{count}: {-1}")