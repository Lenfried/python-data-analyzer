from storage import save_numbers, load_numbers, save_report, print_report
from analyzer import analyze_numbers


def collect_numbers():
    numbers = []
    count = int(input("How many numbers would you like to enter?: "))
    while True:
        if count > 0:
            break
        try:
            count = int(input("Please enter a positive integer for how many numbers you'd like to enter: "))
            if count <= 0:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("You entered the following numbers:")
    for num in numbers:
        print(num, end=" ")
        print()
    
    

    return numbers


def main():

    # show menu options
    #1) Enter numbers and analyze
    #2) Exit the program
    # Ask user to choose an option
    numbers = []
    last_results = None
    while True:
        print("\nMenu:")
        print("1) Enter numbers")
        print("2) Save numbers to JSON file")
        print("3) Load numbers from JSON file")
        print("4) Analyze current numbers")
        print("5) Save analysis report to report.txt")
        print("6) Exit the program")
        choice = input("Please choose an option (1, 2, 3, 4, 5, or 6): ")
        if choice == "1":
            numbers = collect_numbers()
        elif choice == "2":
            try:
                save_numbers(numbers)
            except Exception as e:
                print(f"Failed to save numbers: {e}")
            else:
                print("Numbers saved to data.json")
        elif choice == "3":
            try:
                numbers = load_numbers()
            except Exception as e:
                print(f"Failed to load numbers: {e}")
            else:
                print("Numbers loaded from data.json")
        elif choice == "4":
            if not numbers:
                print("No numbers to analyze. Please enter or load numbers first.")
                continue
            last_results = analyze_numbers(numbers)
            if last_results is None:
                print("No numbers to analyze.")
            #print last_results in a formatted way
            else:
                print_report(numbers, last_results) 


        elif choice == "5":
            if not numbers or last_results is None:
                print("No analysis results to save. Please analyze numbers first.")
                continue
            try:
                save_report(numbers, last_results)
            except Exception as e:
                print(f"Failed to save report: {e}")

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
    


if __name__ == "__main__":
    main()

