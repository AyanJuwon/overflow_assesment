def sort_text():
    return

# get the teext
# collect like characters?>?
# maybe a list
# for each item in list joim char1 and len of the ole strong 

def compress(input_string):
    """

    Parameters:
        input_string (str): The input string to be compressed.
    
    Returns:
        str: The compressed string or the original string if compression
             doesn't reduce the length.
    """
    compressed = []
    count = 1

    for i in range(len(input_string)):
        # If last character matches the next one
        if i < len(input_string) - 1 and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            # Append the character and its count to the compressed list
            compressed.append(input_string[i] + str(count))
            count = 1

    # Join the compressed characters and counts into a string
    compressed_string = ''.join(compressed)

    # Return the compressed string only if it's shorter than the original
    if len(compressed_string) < len(input_string):
        return compressed_string
    else:
        return input_string
    
# Example usage
input_str = "aaaabbbccddddddee"
compressed_str = compress(input_str)
print(compressed_str)  # Output: "a4b3c2d6e2"


# time complexity explanation
# The string compression algorithm has a time complexity of O(n),
# where n is the length of the input string.
# It iterates through the string once (O(n)),
# appends characters and counts to a list (O(n)),
# and then joins the compressed characters (O(n)).
# Overall, it operates linearly with the length of the input string.