def reverse_string(s: str) -> str:
    # Initialize an empty list to act as a stack
    stack = []
    
    # Push all characters of the string into the stack
    for char in s:
        stack.append(char)
    
    # Pop all characters from the stack to form the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Test the function
input_string = "hello"
output_string = reverse_string(input_string)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")
