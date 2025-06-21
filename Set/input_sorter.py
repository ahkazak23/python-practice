
def menu():
    print("What do you want to do?")
    print("1. Show unique values")
    print("2. Show duplicate values")
    print("3. Check membership")
    choice = input("Choose (1–3): ")
    return choice

def get_input():
    values = input("Enter your values (comma-separated): ")
    return [v.strip() for v in values.split(",")]

def show_unique(values):
    unique_values = set(values)
    print("Unique values:", ", ".join(unique_values))

def show_duplicates(values):
    seen = set()
    duplicates = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    print("Duplicates:", ", ".join(duplicates) if duplicates else "No duplicates found")

def check_membership(values):
    value_to_check = input("Enter value to check: ").strip()
    if value_to_check in values:
        print("Result: Found")
    else:
        print("Result: Not found")

def main():
    values = get_input()

    while True:
        choice = menu()

        if choice == '1':
            show_unique(values)
        elif choice == '2':
            show_duplicates(values)
        elif choice == '3':
            check_membership(values)
        else:
            print("Invalid choice. Please try again.")

        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()