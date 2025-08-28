# File Read & Write Challenge with Error Handling

# Ask the user for the input filename
input_file = input("Enter the name of the file to read: ")

try:
    # Try to open the file for reading
    with open(input_file, "r") as file:
        content = file.read()  # Read entire file
        print("\nOriginal file content:")
        print(content)

    # Modify content: for example, convert it to uppercase
    modified_content = content.upper()

    # Define output filename
    output_file = "modified_" + input_file

    # Write modified content to a new file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"\nModified content has been written to '{output_file}'.")

except FileNotFoundError:
    print(f"❌ Error: The file '{input_file}' does not exist.")
except IOError:
    print(f"❌ Error: Cannot read/write the file '{input_file}'.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
