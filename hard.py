def count_digit_one(n: int) -> int:
    """
    Count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

    Args:
    - n (int): The input non-negative integer.

    Returns:
    - int: The total count of digit 1 occurrences.
    """
    count = 0
    factor = 1

    while factor <= n:
        # Divide n by a power of 10 to consider each digit individually
        divmod_result = divmod(n, 10 * factor)
        quotient, remainder = divmod_result

        # Count the occurrences of digit 1 for the current digit place
        count += quotient * factor + min(max(remainder - factor + 1, 0), factor)
        

        # Move to the next digit place
        factor *= 10

    return count

def main():
    # Take input from the user
    user_input = int(input("Enter a non-negative integer (n): "))

    # Check if the input is within the specified constraints
    if 0 <= user_input <= 10**9:
        result = count_digit_one(user_input)
        print(f"The total number of digit 1 appearing in all non-negative integers less than or equal to {user_input} is: {result}")
    else:
        print("Invalid input. Please enter a non-negative integer within the specified constraints.")

if __name__ == "__main__":
    main()
