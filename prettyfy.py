def prettyfy(filename):
    """
    Simple fucntion to pretify the output of GetChildBlock
    """
    with open(filename, 'r') as file:
        content = file.read()

    # Replace tabs followed by '$' with '\n$'
    modified_content = content.replace('\t$', '\n$')

    with open(filename, 'w') as file:
        file.write(modified_content)

    print("Tabs followed by '$' replaced with newline and '$' in", filename)

# Usage example: Replace tabs with newline and '$' in 'myfile.txt'
if __name__ == "__main__":
    prettyfy("GetChildBlocks2.txt")
    print("Done")
