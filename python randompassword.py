import secrets
import string


def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    character_pools = []
    guaranteed_characters = []

    if use_letters:
        character_pools.append(string.ascii_letters)
        guaranteed_characters.append(secrets.choice(string.ascii_letters))

    if use_digits:
        character_pools.append(string.digits)
        guaranteed_characters.append(secrets.choice(string.digits))

    if use_symbols:
        character_pools.append(string.punctuation)
        guaranteed_characters.append(secrets.choice(string.punctuation))

    if not character_pools:
        raise ValueError("At least one character type must be selected.")

    if length < len(guaranteed_characters):
        raise ValueError(f"Length must be at least {len(guaranteed_characters)} to include all selected types.")

    all_characters = "".join(character_pools)

    remaining_length = length - len(guaranteed_characters)
    password_pool = [secrets.choice(all_characters) for _ in range(remaining_length)]

    final_password_list = guaranteed_characters + password_pool

    secrets.SystemRandom().shuffle(final_password_list)

    return "".join(final_password_list)


def main():
    print("--- Advanced Password Generator ---")

    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 4:
                print("Password length must be at least 4.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        use_letters = input("Include letters? (yes/no): ").lower() == "yes"
        use_digits = input("Include numbers? (yes/no): ").lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

        try:
            password = generate_password(length, use_letters, use_digits, use_symbols)
            print("\nGenerated password:")
            print(password)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        again = input("\nGenerate another password? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "_main_":
    main()