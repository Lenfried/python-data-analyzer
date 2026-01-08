
def analyze_numbers(numbers):
    # This function takes a list of numbers and returns basic statistics.
    if not numbers:
        return None
    

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    return {
        "total": total,
        "count": count,
        "average": average,
        "min": minimum,
        "max": maximum
    }


def main():
    # This function collects a series of numbers from the user and displays them.

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
    
    results = analyze_numbers(numbers)
    if results:
        print("\nStatistics:")
        print(f"Total: {results.get('total')}")
        print(f"Count: {results.get('count')}")
        print(f"Average: {results.get('average'):.2f}")
        print(f"Minimum: {results.get('min')}")
        print(f"Maximum: {results.get('max')}")
    else:
        print("No numbers to analyze.")



    


if __name__ == "__main__":
    main()

