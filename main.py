# Define a function to check if a line is a comment
def is_a_comment(line):
    return line.strip().startswith("#")

# Define a function to identify comments in a file
def identify_lines(file_path):
    # Open the specified file in read mode
    with open(file_path, 'r') as file:
        # Read all lines from the file into a list
        lines = file.readlines()

        # Iterate through each line in the list
        for line_number, line in enumerate(lines, start=1):
            # Check if the line is a comment using the is_comment function
            if is_a_comment(line):
                # If it's a comment, print the line number and the comment content
                print(f"Line {line_number}: Comment - {line.strip()}")
            else:
                # If it's not a comment, print the line number and the code content
                print(f"Line {line_number}: Not a Comment - {line.strip()}")


if __name__ == "__main__":
    # Specify the path to the file you want to analyze
    file_path = r'C:\python\identifier\test.py'
    # Call the identify_lines function to analyze the file
    identify_lines(file_path)
