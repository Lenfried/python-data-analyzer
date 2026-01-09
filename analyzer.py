# analyzer.py - analysis logic for the CLI Data Analyzer 
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

def print_report(numbers, results):
    print("\nAnalysis Report")
    print("----------------")
    print("Numbers Entered:")
    for num in numbers:
        print(num, end=" ")
    print()
    print("\nStatistics:")
    print(f"Total: {results.get('total')}")
    print(f"Count: {results.get('count')}")
    print(f"Average: {results.get('average'):.2f}")
    print(f"Minimum: {results.get('min')}")
    print(f"Maximum: {results.get('max')}")


