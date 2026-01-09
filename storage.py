from datetime import datetime

#create a function save_numbers(numbers, filename="data.json")
#it should save the list of numbers to a JSON file as a dictionary with key "numbers"
#use indent = 2
#overwrite the file if it already exists
#do not print anything in this function
import json
def save_numbers(numbers, filename="data.json"):
    with open(filename, "w") as f:
        json.dump({"numbers": numbers}, f, indent=2)

#create a function load_numbers(filename="data.json")
#it should load the list of numbers from a JSON file and return the list under the "numbers key
#if the file does not exist or is invalid, return an empty list
#do not print anything in this function
def load_numbers(filename="data.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data.get("numbers", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_report(numbers, results):
    with open("report.txt", "w") as f:
        f.write(f"Analysis Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("Numbers Entered:\n")
        for num in numbers:
            f.write(f"{num}\n")
        f.write("\nStatistics:\n")
        f.write(f"Total: {results.get('total')}\n")
        f.write(f"Count: {results.get('count')}\n")
        f.write(f"Average: {results.get('average'):.2f}\n")
        f.write(f"Minimum: {results.get('min')}\n")
        f.write(f"Maximum: {results.get('max')}\n")
    print("\nAnalysis report saved to report.txt")
    