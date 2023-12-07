
def length_of_last_word(s: str) -> int:
    words = s.strip().split()
    return len(words[-1]) if words else 0

def get_user_input() -> str:
    while True:
        try:
            user_input = input("Enter a string: ").strip()
            if 1 <= len(user_input) <= 10**4 and all(char.isalpha() or char.isspace() for char in user_input):
                return user_input
            else:
                print("Invalid input. Please make sure the length is between 1 and 10,000, and the string consists of only English letters and spaces.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        user_input = get_user_input()
        result = length_of_last_word(user_input)
        if result > 0:
            print(f"The length of the last word is: {result}")
    except KeyboardInterrupt:
        print("\nExiting program.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        













