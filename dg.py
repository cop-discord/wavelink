import re
import sys

def downgrade_type_hints(file_path):
    # Define the regex pattern to match type hints in Python 3.10+ style
    # This pattern matches types that can be generic (like list, dict, etc.)
    pattern = r'(\w+\[[^\]]*\])\s*\|\s*None'

    # Define the replacement pattern using Optional
    replacement = r'Optional[\1]'

    try:
        # Read the content of the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace type hints using regex
        modified_content = re.sub(pattern, replacement, content)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Type hints in '{file_path}' have been downgraded successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python downgrade_type_hints.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    downgrade_type_hints(file_path)

