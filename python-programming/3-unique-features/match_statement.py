def process_data(data):
    match data:
        case 0 | None:
            return "No data"
        case [first, second]:
            return f"Two elements: {first}, {second}"
        case {"name": name, "age": age}:
            return f"Name: {name}, Age: {age}"
        case int() | float() as number if number > 0:
            return f"Positive number: {number}"
        case str() as text if text.isalpha():
            return f"Alphabetic string: {text}"
        case _:
            return "Unknown data"

# Example usages:
print(process_data(0))                     # Output: No data
print(process_data([1, 2]))                # Output: Two elements: 1, 2
print(process_data({"name": "Alice", "age": 30}))  # Output: Name: Alice, Age: 30
print(process_data(42))                    # Output: Positive number: 42
print(process_data("Hello"))               # Output: Alphabetic string: Hello
print(process_data([1, 2, 3]))             # Output: Unknown data