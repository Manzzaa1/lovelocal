from typing import List

def find_majority_elements(nums: List[int]) -> List[int]:
    """
    Finds elements that appear more than n/3 times in the given integer array.

    :param nums: The input array of integers.
    :return: List of elements that appear more than n/3 times.
    """

    if not nums:
        return []

    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    # Phase 1: Find potential candidates for majority elements
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Phase 2: Verify candidates and find majority elements
    count1, count2 = 0, 0
    for num in nums:
        if candidate1 is not None and num == candidate1:
            count1 += 1
        elif candidate2 is not None and num == candidate2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

def main():
    # Take input from the user
    nums_str = input("Enter the elements of the array separated by spaces: ")
    nums = list(map(int, nums_str.split()))

    # Find majority elements
    result = find_majority_elements(nums)

    # Display the result
    print("Majority elements:", result)

if __name__ == "__main__":
    main()
