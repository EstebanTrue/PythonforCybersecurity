def generate_greeting(name):
    if name == "Alice":
        print("Special greeting for Alice!")
        return "Hi, Alice!"
    else:
        print(f"Hello, {name}!")
        return f"Hello, {name}!"

# Example usage:
user_name = input("Enter a name: ")
result = generate_greeting(user_name)

# Display the result outside the function
print(result)